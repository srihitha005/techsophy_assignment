def analyze_workflow(metrics):
    # Example: Calculate average durations
    summary = {
        "avg_commit_to_pr": sum(metrics["commit_times"]) / len(metrics["commit_times"]),
        "avg_pr_review": sum(metrics["pr_review_times"]) / len(metrics["pr_review_times"]),
        "avg_build": sum(metrics["build_times"]) / len(metrics["build_times"]),
        "avg_deploy": sum(metrics["deploy_times"]) / len(metrics["deploy_times"]),
    }
    return summary
