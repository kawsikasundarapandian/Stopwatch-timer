!pip install gradio

import gradio as gr
import time
start_time = None
elapsed_time = 0
running = False

def start_stopwatch():
    global start_time, running
    if not running:
        start_time = time.time() - elapsed_time
        running = True
    return get_time()

def stop_stopwatch():
    global elapsed_time, running
    if running:
        elapsed_time = time.time() - start_time
        running = False
    return get_time()

def reset_stopwatch():
    global start_time, elapsed_time, running
    start_time = None
    elapsed_time = 0
    running = False
    return "00:00:00"

def get_time():
    global elapsed_time, running
    if running:
        elapsed_time = time.time() - start_time
    mins, secs = divmod(int(elapsed_time), 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"

with gr.Blocks() as demo:
    with gr.Row():
        output = gr.Textbox(label="Stopwatch", value="00:00:00")

    with gr.Row():
        start_btn = gr.Button("Start ⏱️")
        stop_btn = gr.Button("Stop ⛔")
        reset_btn = gr.Button("Reset 🔄")

    start_btn.click(fn=start_stopwatch, outputs=output)
    stop_btn.click(fn=stop_stopwatch, outputs=output)
    reset_btn.click(fn=reset_stopwatch, outputs=output)

demo.launch()
