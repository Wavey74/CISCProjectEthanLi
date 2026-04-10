import gradio as gr
import matplotlib.pyplot as plt
from merge_sort import merge_sort


def create_bar_chart(stops, title):

    names = [stop[0] for stop in stops]
    crowds = [stop[1] for stop in stops]

    fig = plt.figure()
    plt.bar(names, crowds)
    plt.title(title)
    plt.xlabel("Shuttle Stop")
    plt.ylabel("Crowd Count")

    return fig


def process_input(text):

    if not text.strip():
        return "Error: Please enter shuttle stop data.", None

    stops = []

    try:
        lines = text.strip().split("\n")

        for line in lines:
            name, crowd = line.split(",")
            stops.append((name.strip(), int(crowd)))

    except:
        return "Error: Invalid format. Use stop_name,crowd_count", None

    steps = []

    sorted_stops = merge_sort(stops, steps)

    output = "Sorting Steps:\n\n"

    for step in steps:
        formatted = ", ".join([f"{s[0]}({s[1]})" for s in step])
        output += formatted + "\n"

    output += "\nFinal Ranked Stops:\n"

    for i, stop in enumerate(sorted_stops):
        output += f"{i+1}. {stop[0]} — {stop[1]}\n"

    # create chart of final result
    chart = create_bar_chart(sorted_stops, "Final Sorted Stops")

    return output, chart


demo = gr.Interface(
    fn=process_input,
    inputs=gr.Textbox(
        lines=8,
        label="Enter shuttle stops (stop_name,crowd_count)",
        placeholder="Library,45\nResidence,120\nEngineering,30"
    ),
    outputs=[
        gr.Textbox(label="Sorting Output"),
        gr.Plot(label="Crowd Visualization")
    ],
    title="Shuttle Stop Crowd Ranking",
    description="Ranks shuttle stops by crowd size using Merge Sort and visualizes sorting results."
)

demo.launch()