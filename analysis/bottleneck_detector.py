def detect_bottlenecks(metrics_summary):
    bottlenecks = []

    if metrics_summary["avg_pr_review"] > 12:
        bottlenecks.append("PR review time is too high")
    if metrics_summary["avg_deploy"] > 24:
        bottlenecks.append("Deployment time is too high")

    return bottlenecks
