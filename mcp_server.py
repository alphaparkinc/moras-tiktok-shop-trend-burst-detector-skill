import sys, json
from client import TikTokShopTrendBurstDetectorClient
sys.stdout.reconfigure(encoding='utf-8')

def handle_mcp():
    detector = TikTokShopTrendBurstDetectorClient()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps({"status": "ready", "skill": "moras-tiktok-shop-trend-burst-detector-skill"}))
        return
    req = json.loads(sys.stdin.read() or "{}")
    sales = req.get("daily_sales_series", [])
    creators = req.get("active_creator_count", 50)
    asp = req.get("average_selling_price_usd", 20.0)
    res = detector.detect_trend_burst(sales, creators, asp)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    handle_mcp()
