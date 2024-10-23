import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image
import threading

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    input_file_var.set(file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder_var.set(folder_path)

def crop_resize_image(image, size, crop_type='center'):
    original_width, original_height = image.size
    target_width, target_height = size

    if crop_type == 'center':
        aspect_ratio_original = original_width / original_height
        aspect_ratio_target = target_width / target_height

        if aspect_ratio_original > aspect_ratio_target:
            new_width = int(original_height * aspect_ratio_target)
            left = (original_width - new_width) // 2
            right = left + new_width
            image = image.crop((left, 0, right, original_height))
        else:
            new_height = int(original_width / aspect_ratio_target)
            top = (original_height - new_height) // 2
            bottom = top + new_height
            image = image.crop((0, top, original_width, bottom))

    return image.resize((target_width, target_height), Image.LANCZOS)

def process_images():
    input_file = input_file_var.get()
    output_folder = output_folder_var.get()
    convert_to_webp = webp_var.get()

    if not input_file or not output_folder:
        messagebox.showwarning("Input error", "Please select both an input file and an output folder.")
        return

    try:
        image = Image.open(input_file)
    except Exception as e:
        messagebox.showerror("File error", f"Failed to read the image file: {e}")
        return

    selected_sizes = []
    for size_var, size in zip(size_vars, sizes):
        if size_var.get():
            selected_sizes.append(size)

    if not selected_sizes:
        messagebox.showwarning("Input error", "Please select at least one size.")
        return

    file_name, file_extension = os.path.splitext(os.path.basename(input_file))

    def resize_and_save():
        total_images = len(selected_sizes)
        progress_var.set(0)
        progress_step = 100 / total_images

        for idx, size in enumerate(selected_sizes):
            resized_image = crop_resize_image(image, size)
            output_ext = ".webp" if convert_to_webp else file_extension
            output_path = os.path.join(output_folder, f"{file_name}-{size[0]}x{size[1]}{output_ext}")
            save_format = "WEBP" if convert_to_webp else image.format
            resized_image.save(output_path, format=save_format)
            log_table.insert("", "end", values=(f"{file_name}-{size[0]}x{size[1]}{output_ext}", "Completed"))
            progress_var.set(progress_var.get() + progress_step)
            root.update_idletasks()
        messagebox.showinfo("Success", "Images processed successfully!")

    threading.Thread(target=resize_and_save).start()

root = tk.Tk()
root.title("Advanced Image Resizer & WooCommerce Thumbnail Creator")
root.geometry("800x550")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 10), background="#f0f0f0")
style.configure("TButton", font=("Arial", 10))
style.configure("TCheckbutton", font=("Arial", 10), background="#f0f0f0")

input_file_var = tk.StringVar()
output_folder_var = tk.StringVar()
webp_var = tk.BooleanVar()
progress_var = tk.DoubleVar()

sizes = [
    (150, 150),   # Thumbnail
    (300, 300),   # Medium
    (768, 768),   # Medium Large
    (1024, 1024), # Large
    (600, 314),   # WooCommerce Single Product
    (450, 450)    # WooCommerce Gallery Thumbnail
]

size_vars = [tk.BooleanVar() for _ in sizes]

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

input_label = ttk.Label(frame, text="Select input image file:")
input_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
input_entry = ttk.Entry(frame, textvariable=input_file_var, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))
input_browse = ttk.Button(frame, text="Browse", command=select_input_file)
input_browse.grid(row=0, column=2, padx=10, pady=5, sticky=tk.E)

output_label = ttk.Label(frame, text="Select output folder:")
output_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
output_entry = ttk.Entry(frame, textvariable=output_folder_var, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))
output_browse = ttk.Button(frame, text="Browse", command=select_output_folder)
output_browse.grid(row=1, column=2, padx=10, pady=5, sticky=tk.E)

sizes_label = ttk.Label(frame, text="Select crop sizes:")
sizes_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

select_all_var = tk.BooleanVar()

def toggle_select_all():
    for size_var in size_vars:
        size_var.set(select_all_var.get())

select_all_checkbox = ttk.Checkbutton(frame, text="Select All Sizes", variable=select_all_var, command=toggle_select_all)
select_all_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

sizes_frame = ttk.Frame(frame)
sizes_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky=(tk.W, tk.E))

for i, (size_var, size) in enumerate(zip(size_vars, sizes)):
    ttk.Checkbutton(sizes_frame, text=f"{size[0]}x{size[1]}", variable=size_var).grid(row=i//3, column=i%3, padx=10, pady=5, sticky=tk.W)

webp_checkbox = ttk.Checkbutton(frame, text="Convert to WebP", variable=webp_var)
webp_checkbox.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

progress_bar = ttk.Progressbar(frame, variable=progress_var, maximum=100)
progress_bar.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky=(tk.W, tk.E))

log_table = ttk.Treeview(frame, columns=("Filename", "Status"), show="headings", height=5)
log_table.heading("Filename", text="Filename")
log_table.heading("Status", text="Status")
log_table.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky=(tk.W, tk.E))

github_link = ttk.Label(frame, text="PR-M", font=("Arial", 10, "underline"), foreground="blue", cursor="hand2")
github_link.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)
github_link.bind("<Button-1>", lambda e: os.system("start https://github.com/Scary-technologies"))

process_button = ttk.Button(frame, text="Process", command=process_images)
process_button.grid(row=9, column=1, padx=10, pady=20, sticky=tk.E)

root.mainloop()
