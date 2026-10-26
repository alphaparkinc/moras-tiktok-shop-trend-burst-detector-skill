import sys, math
sys.stdout.reconfigure(encoding='utf-8')

class TikTokShopTrendBurstDetectorClient:
    """
    Social commerce product velocity and viral burst prediction engine.
    Calculates 1st order velocity (dSales/dt) and 2nd order acceleration (d^2Sales/dt^2)
    across a time-series window to detect explosive exponential inflection points
    before creator market saturation.
    """
    def __init__(self, saturation_creator_count=500):
        self.saturation_limit = saturation_creator_count

    def detect_trend_burst(self, daily_sales_series, active_creator_count, average_selling_price_usd):
        """
        daily_sales_series: list of int/float sales numbers over recent days (min 4 days)
        active_creator_count: number of active affiliates promoting the SKU
        """
        if len(daily_sales_series) < 3:
            return {"status": "error", "message": "At least 3 consecutive days of sales data required"}

        # 1. Compute velocity (daily delta)
        velocities = [daily_sales_series[i] - daily_sales_series[i-1] for i in range(1, len(daily_sales_series))]
        recent_velocity = velocities[-1]
        prev_velocity = velocities[-2] if len(velocities) >= 2 else 0.0

        # 2. Compute acceleration (delta of delta)
        acceleration = recent_velocity - prev_velocity

        # 3. Market Saturation Index
        saturation_ratio = min(1.0, active_creator_count / float(self.saturation_limit))
        saturation_factor = 1.0 - (saturation_ratio * 0.7) # Diminishes burst upside if overcrowded

        # 4. Composite Viral Burst Score (0 - 100)
        base_growth_rate = (recent_velocity / max(1.0, daily_sales_series[-2])) if daily_sales_series[-2] > 0 else 1.0
        raw_score = (max(0.0, base_growth_rate) * 35.0) + (max(0.0, acceleration) * 0.15)
        viral_burst_score = max(0.0, min(100.0, raw_score * saturation_factor))

        # Opportunity phase assessment
        if saturation_ratio < 0.25 and acceleration > 0:
            stage = "EARLY_INFLECTION_GOLDEN_WINDOW"
            action = "AGGRESSIVE_SCALE_AFFILIATE_CREATIVE"
        elif saturation_ratio < 0.65 and recent_velocity > 0:
            stage = "EXPONENTIAL_GROWTH_PHASE"
            action = "MAINTAIN_CONTENT_VOLUME"
        elif saturation_ratio >= 0.65:
            stage = "LATE_STAGE_CREATOR_SATURATION"
            action = "PIVOT_ANGLE_OR_NEW_SKU"
        else:
            stage = "STAGNANT_OR_DECLINING"
            action = "MONITOR_OR_ABANDON"

        daily_gmv_run_rate = daily_sales_series[-1] * average_selling_price_usd

        return {
            "status": "success",
            "current_daily_sales": daily_sales_series[-1],
            "daily_gmv_run_rate_usd": round(daily_gmv_run_rate, 2),
            "recent_daily_velocity": round(recent_velocity, 1),
            "recent_acceleration": round(acceleration, 1),
            "active_creator_count": active_creator_count,
            "market_saturation_pct": round(saturation_ratio * 100, 1),
            "viral_burst_score": round(viral_burst_score, 1),
            "lifecycle_stage": stage,
            "recommended_strategy": action
        }
