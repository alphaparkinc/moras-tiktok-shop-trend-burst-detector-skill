from client import TikTokShopTrendBurstDetectorClient
import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    detector = TikTokShopTrendBurstDetectorClient()
    print("=== MORAS TIKTOK SHOP TREND BURST DETECTOR ===")

    # 7-day sales progression for a breakout beauty gadget
    recent_7_days_sales = [120, 145, 190, 260, 390, 620, 1050]
    creators = 85
    asp = 24.99

    res = detector.detect_trend_burst(recent_7_days_sales, active_creator_count=creators, average_selling_price_usd=asp)
    print()
    print(f"Current Daily Units : {res['current_daily_sales']} (GMV: ${res['daily_gmv_run_rate_usd']:,.2f}/day)")
    print(f"Sales Velocity      : +{res['recent_daily_velocity']} units/day")
    print(f"Growth Acceleration : +{res['recent_acceleration']} units/day^2")
    print(f"Creator Saturation  : {res['market_saturation_pct']}% ({res['active_creator_count']} affiliates)")
    print(f"Viral Burst Score   : {res['viral_burst_score']}/100")
    print(f"Lifecycle Stage     : {res['lifecycle_stage']}")
    print(f"Action Playbook     : {res['recommended_strategy']}")

if __name__ == "__main__":
    main()
