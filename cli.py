from bot import BasicBot

API_KEY = "4ae8e84a886e567ec92b4c8720c46a6ac04788bff894b0a85a8204335e739ee5"
API_SECRET = "c636eb81e5706105c8ee116d42ca5bf02b9ae035fe2d5d10457cda4b0488febe"

def main():
    bot = BasicBot(API_KEY, API_SECRET)

    print("\n📊 Welcome to the Python Trading Bot")
    print("--------------------------------------")
    print("Supported Order Types: MARKET | LIMIT | STOP_MARKET\n")

    symbol = input("🔹 Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("🔹 Enter side (BUY or SELL): ").upper()
    order_type = input("🔹 Enter order type: ").upper()
    quantity = float(input("🔹 Enter quantity: "))

    price = None
    stop_price = None

    if order_type == 'LIMIT':
        price = float(input("🔹 Enter limit price: "))
    elif order_type == 'STOP_MARKET':
        stop_price = float(input("🔹 Enter stop price: "))

    print("\n📨 Placing order...")
    order = bot.place_order(symbol, side, order_type, quantity, price, stop_price)

    if order:
        print("✅ Order placed successfully:")
        print(order)
    else:
        print("❌ Order failed. See log for details.")

if __name__ == '__main__':
    main()
