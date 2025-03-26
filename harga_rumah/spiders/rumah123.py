from os import path
from re import findall

from scrapy import Spider


class Rumah123Spider(Spider):
    name = "rumah123"
    allowed_domains = ["rumah123.com"]
    start_urls = [
        f"https://www.rumah123.com/jual/balikpapan/rumah/?page={x}"
        for x in range(1, 57)
    ]

    def is_property_page(self, url):
        # Check if URL is a property page
        return "/properti" in url and "/perumahan-baru" not in url

    def parse(self, response):
        # If this is a property page, scrape detailed information
        if self.is_property_page(response.url):
            yield {
                "id": self.extract_id(response),
                "price": self.extract_price(response),
                "installment": self.extract_installment(response),
                "address": self.extract_address(response),
                "tags": self.extract_tags(response),
                "specs": self.extract_specs(response),
                "agent": self.extract_property_agent(response),
            }
        else:
            # If this is a pagination page, extract property URLs and follow them
            for property_url in response.xpath(
                "//div[contains(@class, 'ui-organism-intersection__element intersection-card-container')]//a/@href"
            ).getall():
                if self.is_property_page(property_url):
                    yield response.follow(property_url)

    def extract_id(self, response):
        return path.basename(path.normpath(response.url))

    def extract_price(self, response):
        price = response.xpath(
            "//div[@class='pl-1 py-1.5 grow md:grow-0 -ml-1 flex-auto md:flex-none']/p[@class='text-sm text-primary mb-1 font-semibold line-clamp-1']/text()"
        ).get()

        if not price:
            return None

        components = price.strip().split(" ")
        unit = components[2].lower()
        price_value = float(components[1].replace(",", ""))

        if "miliar" in unit:
            return price_value * 1000
        elif "juta" in unit:
            return price_value
        else:
            return None

    def extract_installment(self, response):
        # Extract the full text of the <p> tag (including child nodes)
        installment_text = response.xpath(
            "//p[contains(@class, 'text-gray-400') and contains(text(), 'Cicilan')]//text()"
        ).getall()

        # Join the text fragments into a single string
        installment_text = " ".join(installment_text).strip()

        # Debugging: Print the extracted text
        print(f"Installment Text: {installment_text}")

        if not installment_text:
            return None

        # Extract the numeric value using regex
        installment_values = findall(r"\d+(?:,\d+)?", installment_text)
        if not installment_values:
            return None

        # Convert the value to a float
        installment_value = float(installment_values[0].replace(",", "."))

        # Check if the unit is "Jutaan" or "Miliaran"
        if "Jutaan" in installment_text:
            return installment_value  # Already in juta
        elif "Miliaran" in installment_text:
            return installment_value * 1000  # Convert to juta
        else:
            return None

    def extract_address(self, response):
        return response.xpath("//p[@class='text-xs text-gray-500 mb-2']/text()").get()

    def extract_tags(self, response):
        tags = response.xpath(
            "//div[contains(@class, 'w-fit text-xs leading-4 font-normal py-1.5 px-2 rounded-full !bg-secondary text-accent')]/text()"
        ).getall()
        return [tag.strip() for tag in tags]

    def extract_images(self, response):
        for current_src in response.xpath("//img/@src").getall():
            if "/customer/" in current_src:
                yield current_src

    def extract_description(self, response):
        return response.xpath(
            "//p[@class='text-sm font-light mb-6 whitespace-pre-wrap leading-6 text-gray-600']/text()"
        ).get()

    def extract_specs(self, response):
        specs = {}
        spec_elements = response.xpath(
            "//div[contains(@class, 'mb-4 flex items-center gap-4 text-sm border-0 border-b border-solid border-gray-200 pb-2 last:border-b-0')]"
        )
        for spec in spec_elements:
            key = spec.xpath(
                ".//p[@class='w-32 text-xs font-light text-gray-500']/text()"
            ).get()
            value = spec.xpath(".//p[not(@class)]/text()").get()
            if key and value:
                specs[key.strip()] = value.strip()
        return specs

    def extract_property_agent(self, response):
        agent = {}

        # Extract agent name
        agent_name = response.xpath(
            "//div[contains(@class, 'flex flex-col py-6 px-4 rounded-2xl bg-white shadow-md gap-4')]//div[contains(@class, 'text-base text-primary font-semibold')]/text()"
        ).get()
        if agent_name:
            agent["name"] = agent_name.strip()

        # Extract agent phone number
        agent_phone = response.xpath(
            "//div[contains(@class, 'flex flex-col py-6 px-4 rounded-2xl bg-white shadow-md gap-4')]//button[@name='phone']/span[contains(@class, 'line-clamp-1')]/text()"
        ).get()
        if agent_phone:
            agent["phone"] = agent_phone.strip()

        # Extract agent company name
        agent_company = response.xpath(
            "//div[contains(@class, 'flex flex-col py-6 px-4 rounded-2xl bg-white shadow-md gap-4')]//a[contains(@title, 'Brighton First')]/@title"
        ).get()
        if agent_company:
            agent["company"] = agent_company.strip()

        return agent
