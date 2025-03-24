import os
import json
import shutil

# Define paths
training_dir = "../data/training"
output_dir = "../data/training_wo_output"
replacement_output = "Searching this. Find out how to create this output."

# Clear output directory if it exists
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
    print(f"Cleared existing directory: {output_dir}")

# Create output directory
os.makedirs(output_dir, exist_ok=True)
print(f"Created fresh output directory: {output_dir}")
  
# Process all JSON files in the training directory
for filename in os.listdir(training_dir):
    if filename.endswith(".json"):
        # Read the JSON file
        input_file_path = os.path.join(training_dir, filename)
        with open(input_file_path, 'r') as f:
            data = json.load(f)
        
        # Modify the data: replace test output with "Searching"
        if "test" in data:
            for test_case in data["test"]:
                if "output" in test_case:
                    test_case["output"] = replacement_output
        
        # Write the modified JSON to the output directory
        # Create new filename with "modified" before the extension
        base_name = os.path.splitext(filename)[0]
        new_filename = f"{base_name}_modified.json"
        output_file_path = os.path.join(output_dir, new_filename)
        with open(output_file_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"Processed {filename} -> {new_filename}")

print(f"All files processed and saved to {output_dir}")
