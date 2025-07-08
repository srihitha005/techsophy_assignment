# def suggest_recommendations(bottlenecks):
#     recommendations = []

#     for bottleneck in bottlenecks:
#         if "PR review" in bottleneck:
#             recommendations.append("Encourage smaller PRs, assign reviewers early, and set clear SLAs for review times.")
#         if "Deployment" in bottleneck:
#             recommendations.append("Automate deployment processes and consider using canary or blue-green deployments to speed up safely.")

#     return recommendations

def suggest_recommendations(bottlenecks):
    recommendations = []

    for bottleneck in bottlenecks:
        if "PR review" in bottleneck:
            recommendations.append(
                "Reduce PR review time by introducing code ownership, automating reviewer assignment, providing reviewer training, and tracking review SLAs in dashboards."
            )
        if "Deployment" in bottleneck:
            recommendations.append(
                "Shorten deployment time by investing in deployment pipeline optimization, parallelizing steps, introducing advanced strategies like canary releases, and setting automated rollback policies."
            )
        if "Build" in bottleneck:
            recommendations.append(
                "Improve build performance by caching dependencies, using incremental builds, and optimizing CI/CD configurations."
            )
        if "Commit to PR" in bottleneck:
            recommendations.append(
                "Encourage developers to create PRs sooner after commits, enforce branch policies, and provide early feedback via draft PRs."
            )

    return recommendations
