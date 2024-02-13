# INSTALL LIBRARY
!pip install -q gradio

# IMPORT LIBRARY
import gradio as gr

# INCLUDE AT END OF APP.PY
demo.launch()

# TEXT BOX
import gradio as gr

with gr.Blocks() as demo:
    gr.Textbox()

# DEAULT BUTTON
with gr.Blocks() as demo:
   gr.Button()

# CLEAR BUTTON
with gr.Blocks() as demo:
    textbox = gr.Textbox(value="This is some text")
    gr.ClearButton(textbox)

if __name__ == "__main__":

# UPLOAD BUTTON (.txt & .csv)
def upload_file(files):
  file_paths = [file.name for file in files]
  return file_paths

with gr.Blocks() as demo:
  file_output = gr.File()
  upload_button = gr.UploadButton("Click to Upload a File", file_types=["txt", "csv"], file_count="multiple")
  upload_button.upload(upload_file, upload_button, file_output)

# CHECKBOX
with gr.Blocks() as demo:
  gr.Checkbox()

# CHECKBOX GROUP
with gr.Blocks() as demo:
  gr.CheckboxGroup(choices=["First Choice", "Second Choice", "Third Choice"])

# RADIO CHOICES
with gr.Blocks() as demo:
  gr.Radio(choices=["First Choice", "Second Choice", "Third Choice"])

# PROGRESS BAR
import time

def load_set(progress=gr.Progress()):
    imgs = [None] * 24
    for img in progress.tqdm(imgs, desc="Loading..."):
        time.sleep(0.1)
    return "Loaded"


with gr.Blocks() as demo:
    load = gr.Button("Load")
    label = gr.Label(label="Loader")
    load.click(load_set, outputs=label)

demo.queue(concurrency_count=20).launch()

# DROPDOWN MENU
with gr.Blocks() as demo:
  gr.Dropdown(choices=["First Choice", "Second Choice", "Third Choice"])

# MARKDOWN
with gr.Blocks() as demo:
  gr.Markdown(value="This _example_ was **written** in [Markdown](https://en.wikipedia.org/wiki/Markdown)\n")

# NUMBERS
with gr.Blocks() as demo:
  gr.Number()

# WEBCAM CAPTURE
def snap(image, video):
  return [image, video]


demo = gr.Interface(
  snap,
  [gr.Image(source="webcam", tool=None), gr.Video(source="webcam")],
  ["image", "video"],
)

if __name__ == "__main__":

# CANCEL EVENTS
import time
import gradio as gr


def fake_diffusion(steps):
    for i in range(steps):
        print(f"Current step: {i}")
        time.sleep(0.2)
        yield str(i)


def long_prediction(*args, **kwargs):
    time.sleep(10)
    return 42


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            n = gr.Slider(1, 10, value=9, step=1, label="Number Steps")
            run = gr.Button(value="Start Iterating")
            output = gr.Textbox(label="Iterative Output")
            stop = gr.Button(value="Stop Iterating")
        with gr.Column():
            textbox = gr.Textbox(label="Prompt")
            prediction = gr.Number(label="Expensive Calculation")
            run_pred = gr.Button(value="Run Expensive Calculation")
        with gr.Column():
            cancel_on_change = gr.Textbox(label="Cancel Iteration and Expensive Calculation on Change")
            cancel_on_submit = gr.Textbox(label="Cancel Iteration and Expensive Calculation on Submit")
            echo = gr.Textbox(label="Echo")
    with gr.Row():
        with gr.Column():
            image = gr.Image(source="webcam", tool="editor", label="Cancel on edit", interactive=True)
        with gr.Column():
            video = gr.Video(source="webcam", label="Cancel on play", interactive=True)

    click_event = run.click(fake_diffusion, n, output)
    stop.click(fn=None, inputs=None, outputs=None, cancels=[click_event])
    pred_event = run_pred.click(fn=long_prediction, inputs=[textbox], outputs=prediction)

    cancel_on_change.change(None, None, None, cancels=[click_event, pred_event])
    cancel_on_submit.submit(lambda s: s, cancel_on_submit, echo, cancels=[click_event, pred_event])
    image.edit(None, None, None, cancels=[click_event, pred_event])
    video.play(None, None, None, cancels=[click_event, pred_event])

    demo.queue(concurrency_count=2, max_size=20)

if __name__ == "__main__":
    demo.launch()

# WEB SERVER
import portpicker
import threading
import socket
import IPython

from six.moves import socketserver
from six.moves import SimpleHTTPServer

class V6Server(socketserver.TCPServer):
  address_family = socket.AF_INET6

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    # If the response should not be cached in the notebook for
    # offline access:
    # self.send_header('x-colab-notebook-cache-control', 'no-cache')
    self.end_headers()
    self.wfile.write(b'''
      document.querySelector('#output-area').appendChild(document.createTextNode('Script result!'));
    ''')

port = portpicker.pick_unused_port()

def server_entry():
    httpd = V6Server(('::', port), Handler)
    # Handle a single request then exit the thread.
    httpd.serve_forever()

thread = threading.Thread(target=server_entry)
thread.start()

# Display some HTML referencing the resource.
display(IPython.display.HTML('<script src="https://localhost:{port}/"></script>'.format(port=port)))

# CREATE WEB SERVER IFRAME
from google.colab import output
output.serve_kernel_port_as_iframe(port)

# VIEW WEB SERVER AS NEW BROWSER TAB
from google.colab import output
output.serve_kernel_port_as_window(port)

# CAMERA CAPTURE
from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename


                from IPython.display import Image
                try:
                  filename = take_photo()
                  print('Saved to {}'.format(filename))

                  # Show the image which was just taken.
                  display(Image(filename))
                except Exception as err:
                  # Errors will be thrown if the user does not have a webcam or if they do not
                  # grant the page permission to access it.
                  print(str(err))



