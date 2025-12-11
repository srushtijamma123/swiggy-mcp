from mcp.server.fastmcp import FastMCP
from customers import CUSTOMERS
from orders import ORDERS
from restaurants import RESTAURANTS


server = FastMCP(
    name="swiggy-mcp",
    website_url="https://github.com/srushtijamma123"
)

# ----------------------
# TOOLS
# ----------------------
@server.tool()
def get_customer_summary(customer_id: str) -> dict | None:
    for customer in CUSTOMERS:
        if customer["customerId"] == customer_id:
            return customer
    return None


@server.tool()
def get_order_information(order_id: str) -> dict | None:
    for order in ORDERS:
        if order["orderId"] == order_id:
            return order
    return None


@server.tool()
def get_restaurant_information(id: str) -> dict | None:
    for restaurant in RESTAURANTS:
        if restaurant["id"] == id:
            return restaurant
    return None


def read_markdown_file(file_path: str) -> str | None:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error loading file '{file_path}': {e}"


# ----------------------
# RESOURCES
# ----------------------

@server.resource("policy://refund")
def refund_policy() -> str:
    return read_markdown_file("refundpolicy.md")


@server.resource("complaint://{ctype}")
def get_complaint_resolution(ctype: str) -> str:
    # You can later add: f"Latetimedelivery_{ctype}.md"
    return read_markdown_file("Latetimedelivery.md")



if __name__ == "__main__":
    server.run(transport="stdio")
