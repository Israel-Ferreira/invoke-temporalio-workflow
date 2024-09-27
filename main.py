from flask import Flask, request, jsonify

from temporalio.client import Client

from uuid import uuid4



app =  Flask(__name__)


@app.get("/greetings")
async def greetings():
    name = request.args.get("name")

    if name == "" or name is None:
        name =  "Stranger"


    task_id =  uuid4()



    client =  await Client.connect("localhost:7233")
    

    result = await client.execute_workflow("SendGreetingWorkflow",name, task_queue="greeting-tasks", id=f"greeting-id-work-{task_id}")

    return jsonify({
        "message": result
    })



if __name__ == "__main__":
    app.run()