from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
items = []
next_id = 1


@app.route("/", methods=["GET", "POST"])
def home():
    global next_id
    if request.method == "POST":
        item = {
            "id": next_id,
            "name": request.form.get("name", "").strip(),
            "type": request.form.get("type", ""),
            "description": request.form.get("description", "").strip(),
            "location": request.form.get("location", "").strip(),
            "contact": request.form.get("contact", "").strip(),
        }
        required = ["name", "type", "description", "location", "contact"]
        if all(item[key] for key in required):
            items.append(item)
            next_id += 1
        return redirect(url_for("home"))

    search = request.args.get("search", "").strip().lower()
    filtered_items = [
        item for item in items
        if search in item["name"].lower()
        or search in item["location"].lower()
        or search in item["description"].lower()
        or search in item["type"].lower()
    ]
    return render_template("index.html", items=filtered_items, search=search)


@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
