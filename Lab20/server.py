"""Lab 20: Build the Other Side — Server

Your FastAPI grading server. Build each section as you work
through the tasks. The TODOs tell you what to add and where.
"""

from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse
import uuid

app = FastAPI()
grading_log = []
completed = {}
jobs = {}
job_submission_map = {}

# ---------------------------------------------------------------------------
# Task 1: The Naive Server
# ---------------------------------------------------------------------------
from grading import grade

@app.post("/grade")
def grade_endpoint(data: dict):
    student = data["student"]
    lab = data["lab"]
    slow = data.get("slow", False)
    submission_id = data.get("submission_id")

    if submission_id and submission_id in completed:
        return completed[submission_id]
    
    score = grade(student, lab, slow=slow)

    result = {"student": student, "lab": lab, "score": score}

    grading_log.append(result)

    if submission_id:
        completed[submission_id] = result

    return result 

# ---------------------------------------------------------------------------
# Task 2: Retries Reveal a Problem
# ---------------------------------------------------------------------------
@app.get("/log")
def get_log():
    return {"entries": grading_log}

@app.post("/reset-log")
def reset_log():
    grading_log.clear()
    return {"statud": "cleared"}


# ---------------------------------------------------------------------------
# Task 3: Idempotency Makes Retries Safe
# ---------------------------------------------------------------------------
@app.post("/reset-completed")
def reset_completed():
    completed.clear()
    return {"status": "cleared"}


# ---------------------------------------------------------------------------
# Task 4: Honest About Time
# ---------------------------------------------------------------------------
def run_grade_job(job_id, student, lab):
    score = grade(student, lab, slow=True)
    result = {"student": student, "lab": lab, "score": score}

    grading_log.append(result)

    jobs[job_id] = {"status": "complete", "result": result}


@app.post("/grade-async")
def grade_async(data: dict, background_tasks: BackgroundTasks):
    student = data["student"]
    lab = data["lab"]
    submission_id = data.get("submission_id")

    if submission_id and submission_id in job_submission_map:
        job_id = job_submission_map[submission_id]
        return JSONResponse({"job_id": job_id, "status": "accepted"}, status_code=202)

    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "pending"}

    if submission_id:
        job_submission_map[submission_id] = job_id

    background_tasks.add_task(run_grade_job, job_id, student, lab)

    return JSONResponse({"job_id": job_id, "status": "accepted"}, status_code=202)

@app.get("/grade-jobs/{job_id}")
def get_grade_job(job_id: str):
    if job_id not in jobs:
        return JSONResponse({"error": "job not found"}, status_code=404)
    
    job = jobs[job_id]

    if job["status"] == "pending":
        return {"job_id": job_id, "status": "pending"}
    
    return {
        "job_id": job_id, 
        "status": "complete", 
        "result": job["result"]
    }






# You'll need: from fastapi import BackgroundTasks
#              from fastapi.responses import JSONResponse
#
# Add jobs dict, job_submission_map dict, and a job ID generator.
# Create POST /grade-async (returns 202, runs grading in background).
# Create a run_grade_job helper that does the actual grading.
# Create GET /grade-jobs/{job_id} to check job status.

# TODO: jobs = {}
# TODO: job_submission_map = {}

# TODO: POST /grade-async endpoint

# TODO: run_grade_job helper function

# TODO: GET /grade-jobs/{job_id} endpoint