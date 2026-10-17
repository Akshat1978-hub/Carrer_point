def forecast_demand(history, horizon=5):
    """Linear-trend extrapolation for teaching/demo purposes, not a labour-market forecast."""
    if not history or len(history) < 2:
        raise ValueError("At least two historical values are required.")
    if not isinstance(horizon, int) or horizon not in (1, 3, 5, 10):
        raise ValueError("Horizon must be 1, 3, 5, or 10 years.")
    n = len(history)
    x_mean = (n-1)/2
    y_mean = sum(history)/n
    denom = sum((i-x_mean)**2 for i in range(n))
    slope = sum((i-x_mean)*(y-y_mean) for i,y in enumerate(history))/denom if denom else 0
    values = [max(0, round(history[-1]+slope*step, 2)) for step in range(1, horizon+1)]
    change = ((values[-1]-history[-1])/history[-1]*100) if history[-1] else 0
    return {"forecast":values,"slope":slope,"change_pct":change}
