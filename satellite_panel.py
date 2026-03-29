import customtkinter as ctk
from tkinter import filedialog
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

input_text = None
overview_label = None
result_display = None
is_processing = False
spacecraft_api = None

APP_SIZE = "1200x600"
APP_TITLE = "Data Compression Panel"
FONT = "Trebuchet MS"
INPUT_SIDE_COLOR = "#0f0f0f"
OUTPUT_SIDE_COLOR = "#141414"
PRIMARY_COLOR = "#b3b3b3"
FRAME_COLOR = "#1a1a1a"
BUTTON_TEXT_COLOR = "#1a1a1a"
BUTTON_HOVER_COLOR = "#FFFFFF"
FLASH_PERIOD = 10
FLASH_LIFETIME = 1
FLASH_LUMINOSITY = 100

def show_error(app, message):
    popup = ctk.CTkToplevel(app)
    popup.title("Error")
    popup.geometry("360x160")
    popup.resizable(False, False)
    popup.configure(fg_color="#1a1a1a")
    popup.grab_set()

    app.update_idletasks()
    x = app.winfo_x() + (app.winfo_width() // 2) - 180
    y = app.winfo_y() + (app.winfo_height() // 2) - 80
    popup.geometry(f"360x160+{x}+{y}")

    icon_label = ctk.CTkLabel(popup, text="⚠", font=(FONT, 28), text_color="#e05c5c")
    icon_label.pack(pady=(18, 0))

    msg_label = ctk.CTkLabel(popup, text=message, font=(FONT, 14), text_color="#b3b3b3", wraplength=300)
    msg_label.pack(pady=(6, 0))

    ok_btn = ctk.CTkButton(
        popup, text="OK",
        font=(FONT, 14),
        text_color="#1a1a1a",
        fg_color="#b3b3b3",
        hover_color="#ffffff",
        width=80, height=30,
        command=popup.destroy
    )
    ok_btn.pack(pady=(12, 0))

def app_setup():
    app = ctk.CTk()
    app.geometry(APP_SIZE)
    app.title(APP_TITLE)
    app.resizable(False, False)
    app.configure(fg_color=INPUT_SIDE_COLOR)
    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=3)
    app.rowconfigure(0, weight=1)
    app.iconbitmap("icon.ico")
    return app

def create_widget(mstr, widget_type, **options):
    return widget_type(master=mstr, **options)

def update_overview(text):
    overview_label.delete("0.0", "end")
    overview_label.insert("0.0", text)

def update_result(text):
    result_display.configure(state="normal")
    result_display.delete("0.0", "end")
    result_display.insert("0.0", text)
    result_display.configure(state="disabled")

def compress(text):
    return text

def deliver(compressed_text, api_key, method):
    print(f"Delivering to spacecraft with API: {api_key}")
    print(f"Compression method: {method}")
    print(f"Data: {compressed_text}")

def set_ui_locked(locked, upload_btn, submit_btn, hand_entry, compress_btn):
    state = "disabled" if locked else "normal"
    upload_btn.configure(state=state)
    submit_btn.configure(state=state)
    hand_entry.configure(state=state)
    overview_label.configure(state=state)
    compress_btn.configure(
        state=state,
        text="Compressing..." if locked else "Compress",
        fg_color="#555555" if locked else PRIMARY_COLOR
    )

def input_panel_setup(app):
    global input_text, spacecraft_api

    def on_submit():
        input_text = hand_input_entry.get()
        if not input_text.strip():
            show_error(app, "Please enter some text before submitting.")
            return
        update_overview(input_text)

    def upload_file():
        path = filedialog.askopenfilename(filetypes=[("Text File", "*.txt")])
        if path:
            with open(path, "r") as file:
                input_text = file.read()
                update_overview(input_text)
        else:
            show_error(app, "No file selected or file is invalid.")

    def on_set_api():
        global spacecraft_api
        spacecraft_api = api_entry.get().strip()
        if spacecraft_api:
            if len(spacecraft_api) > 100:
                spacecraft_api = f"{spacecraft_api[:100]}+..."
            api_label.configure(text=f"API: {spacecraft_api}")
        else:
            spacecraft_api = None
            api_label.configure(text="API: [Not Set]")
            show_error(app, "API key cannot be empty.")

    input_side_frame = create_widget(
        app, ctk.CTkFrame,
        corner_radius=0,
        fg_color=INPUT_SIDE_COLOR,
        border_width=0,
    )
    input_side_frame.grid(row=0, column=0, rowspan=100, sticky="nsew")
    input_side_frame.columnconfigure(0, weight=1)
    input_side_frame.rowconfigure(0, weight=1)
    input_side_frame.rowconfigure(1, weight=1)
    input_side_frame.rowconfigure(2, weight=1)
    input_side_frame.rowconfigure(3, weight=1)

    decorative0 = create_widget(input_side_frame, ctk.CTkLabel, text="Upload / Set", font=(FONT, 50), text_color=PRIMARY_COLOR)
    decorative0.grid(row=0, column=0)

    file_upload_frame = create_widget(input_side_frame, ctk.CTkFrame, corner_radius=10, fg_color=FRAME_COLOR, border_width=1, border_color=PRIMARY_COLOR)
    file_upload_frame.grid(row=1, column=0)

    upload_button = create_widget(file_upload_frame, ctk.CTkButton, text="Browse File", font=(FONT, 18), text_color=BUTTON_TEXT_COLOR, fg_color=PRIMARY_COLOR, hover_color=BUTTON_HOVER_COLOR, border_width=0, command=upload_file)
    upload_button.grid(row=0, column=0, padx=10, pady=10)

    decorative1 = create_widget(file_upload_frame, ctk.CTkLabel, text="Supported: .txt", font=(FONT, 13), text_color="#888888")
    decorative1.grid(row=1, column=0, pady=(0, 8))

    hand_input_frame = create_widget(
        input_side_frame, ctk.CTkFrame,
        corner_radius=10,
        fg_color=FRAME_COLOR,
        border_width=1,
        border_color=PRIMARY_COLOR
    )
    hand_input_frame.grid(row=2, column=0)

    hand_input_entry = create_widget(
        hand_input_frame, ctk.CTkEntry,
        placeholder_text="Enter Text",
        width=150,
        border_width=1,
        border_color=PRIMARY_COLOR,
        fg_color=INPUT_SIDE_COLOR
    )
    hand_input_entry.grid(row=0, column=0, padx=10, pady=(10, 5))

    submit_button = create_widget(
        hand_input_frame, ctk.CTkButton,
        text="Submit",
        text_color=BUTTON_TEXT_COLOR,
        fg_color=PRIMARY_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        border_width=0,
        font=(FONT, 16),
        command=on_submit
    )
    submit_button.grid(row=1, column=0, padx=10, pady=(0, 10))

    api_frame = create_widget(
        input_side_frame, ctk.CTkFrame,
        corner_radius=10,
        fg_color=FRAME_COLOR,
        border_width=1,
        border_color=PRIMARY_COLOR
    )
    api_frame.grid(row=3, column=0, pady=(0, 20))

    api_decorative = create_widget(api_frame, ctk.CTkLabel, text="Spacecraft Server Address:", font=(FONT, 16), text_color="#888888")
    api_decorative.grid(row=0, column=0, pady=(10, 0))

    api_entry = create_widget(
        api_frame, ctk.CTkEntry,
        placeholder_text="Enter API key...",
        width=150,
        border_width=1,
        border_color=PRIMARY_COLOR,
        fg_color=INPUT_SIDE_COLOR,
    )
    api_entry.grid(row=1, column=0, padx=10, pady=(5, 5))

    set_api_button = create_widget(
        api_frame, ctk.CTkButton,
        text="Set API",
        text_color=BUTTON_TEXT_COLOR,
        fg_color=PRIMARY_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        border_width=0,
        font=(FONT, 16),
        command=on_set_api
    )
    set_api_button.grid(row=2, column=0, padx=10, pady=(0, 5))

    api_label = create_widget(api_frame, ctk.CTkLabel, text="API: [Not Set]", font=(FONT, 13), text_color="#888888", width=150, wraplength=140)
    api_label.grid(row=3, column=0, pady=(0, 10))

    return upload_button, submit_button, hand_input_entry

def output_panel_setup(app, upload_btn, submit_btn, hand_entry):
    global overview_label, result_display

    output_side_frame = create_widget(
        app, ctk.CTkFrame,
        corner_radius=0,
        fg_color=OUTPUT_SIDE_COLOR,
        border_width=0,
    )
    output_side_frame.grid(row=0, column=1, rowspan=100, sticky="nsew")
    output_side_frame.columnconfigure(0, weight=1)
    output_side_frame.rowconfigure(0, weight=1)
    output_side_frame.rowconfigure(1, weight=1)
    output_side_frame.rowconfigure(2, weight=1)
    output_side_frame.rowconfigure(3, weight=1)
    output_side_frame.rowconfigure(4, weight=1)

    decorative0 = create_widget(output_side_frame, ctk.CTkLabel, text="Compress", font=(FONT, 50), text_color=PRIMARY_COLOR)
    decorative0.grid(row=0, column=0)

    overview_frame = create_widget(output_side_frame, ctk.CTkFrame, corner_radius=10, fg_color=FRAME_COLOR, border_width=1, border_color=PRIMARY_COLOR)
    overview_frame.grid(row=1, column=0)

    decorative1 = create_widget(overview_frame, ctk.CTkLabel, text="Input Text:", font=(FONT, 16), text_color="#888888")
    decorative1.grid(row=0, column=0, pady=(10, 0))

    overview_label = create_widget(
        overview_frame, ctk.CTkTextbox,
        width=400, height=150,
        font=(FONT, 16),
        fg_color=INPUT_SIDE_COLOR,
        border_width=0,
        wrap="word",
    )
    overview_label.grid(row=1, column=0, padx=10, pady=(0, 10))

    compress_frame = create_widget(
        output_side_frame, ctk.CTkFrame,
        fg_color="transparent",
        border_width=0
    )
    compress_frame.grid(row=2, column=0, pady=10)

    method_dropdown = create_widget(
        compress_frame, ctk.CTkOptionMenu,
        values=["Method 1", "Method 2", "Method 3"],
        font=(FONT, 14),
        fg_color=FRAME_COLOR,
        button_color=PRIMARY_COLOR,
        button_hover_color=BUTTON_HOVER_COLOR,
        text_color=PRIMARY_COLOR,
        width=130
    )
    method_dropdown.grid(row=0, column=0, padx=(0, 10))

    compress_btn = create_widget(
        compress_frame, ctk.CTkButton,
        text="Compress",
        text_color=BUTTON_TEXT_COLOR,
        font=(FONT, 18),
        fg_color=PRIMARY_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        border_width=0,
        height=40,
        width=200,
    )
    compress_btn.grid(row=0, column=1)

    def on_compress():
        global is_processing
        current_text = overview_label.get("0.0", "end").strip()
        if not current_text:
            show_error(app, "No input text to compress.\nPlease upload a file or enter text first.")
            return
        is_processing = True
        set_ui_locked(True, upload_btn, submit_btn, hand_entry, compress_btn)
        app.update()
        compressed = compress(current_text)
        update_result(compressed)
        is_processing = False
        set_ui_locked(False, upload_btn, submit_btn, hand_entry, compress_btn)

    compress_btn.configure(command=on_compress)

    result_frame = create_widget(output_side_frame, ctk.CTkFrame, corner_radius=10, fg_color=FRAME_COLOR, border_width=1, border_color=PRIMARY_COLOR)
    result_frame.grid(row=3, column=0)

    decorative2 = create_widget(result_frame, ctk.CTkLabel, text="Compressed Data:", font=(FONT, 16), text_color="#888888")
    decorative2.grid(row=0, column=0, pady=(10, 0))

    result_display = create_widget(
        result_frame, ctk.CTkTextbox,
        width=400, height=150,
        font=(FONT, 16),
        fg_color=INPUT_SIDE_COLOR,
        border_width=0,
        wrap="word"
    )
    result_display.grid(row=1, column=0, padx=10, pady=(0, 5))
    result_display.insert("0.0", "[None]")
    result_display.configure(state="disabled")

    def on_deliver():
        compressed_text = result_display.get("0.0", "end").strip()
        if not compressed_text or compressed_text == "[None]":
            show_error(app, "No compressed data to deliver.\nPlease compress some text first.")
            return
        if not spacecraft_api:
            show_error(app, "Spacecraft API key is not set.\nPlease enter and confirm your API key.")
            return
        selected_method = method_dropdown.get()
        deliver(compressed_text, spacecraft_api, selected_method)

    deliver_button = create_widget(
        result_frame, ctk.CTkButton,
        text="Deliver To Spacecraft",
        text_color=BUTTON_TEXT_COLOR,
        fg_color=PRIMARY_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        border_width=0,
        font=(FONT, 16),
        command=on_deliver
    )
    deliver_button.grid(row=2, column=0, padx=10, pady=(0, 10))

def initialize():
    app = app_setup()
    label = create_widget(app, ctk.CTkLabel, text="Data Compression Panel", font=(FONT, 50), text_color=PRIMARY_COLOR)
    label.place(relx=0.5, rely=0.05, anchor="center")
    upload_btn, submit_btn, hand_entry = input_panel_setup(app)
    output_panel_setup(app, upload_btn, submit_btn, hand_entry)
    app.mainloop()