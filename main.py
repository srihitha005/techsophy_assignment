from fastapi import FastAPI
from data.collector import collect_all_metrics
from analysis.workflow_analyzer import analyze_workflow
from analysis.bottleneck_detector import detect_bottlenecks
from analysis.recommendation_engine import suggest_recommendations

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "DevOps Analyzer API running. Use /analyze to analyze metrics."}

@app.get("/analyze")
async def analyze_team():
    metrics = collect_all_metrics()
    workflow_summary = analyze_workflow(metrics)
    bottlenecks = detect_bottlenecks(workflow_summary)
    recommendations = suggest_recommendations(bottlenecks)
    return {
        "workflow_summary": workflow_summary,
        "bottlenecks": bottlenecks,
        "recommendations": recommendations,
    }
