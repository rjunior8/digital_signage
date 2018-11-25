from flask import Flask, redirect, render_template
import os
import time


app = Flask(__name__)

extra_dirs = ["static",]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
  for dirname, dirs, files in os.walk(extra_dir):
    for filename in files:
      filename = os.path.join(dirname, filename)
      if os.path.isfile(filename):
        extra_files.append(filename)

@app.route('/')
def home():
  refresh = False
  if "WERKZEUG_LOADED" in os.environ:
    refresh = True
  else:
    os.environ["WERKZEUG_LOADED"] = "TRUE"
  video = os.listdir("static")
  return render_template("play.html", video=video, refresh=refresh)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", extra_files=extra_files)
