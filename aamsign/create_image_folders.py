import os

# Base path
base_path = r'e:\AAC\aam-sign\aamsign\static\images'

# Define folder structure
folder_structure = {
    'channel-letters': [
        'front-lit',
        'back-lit',
        'front-back-lit',
        'open-face',
        'non-illuminated',
        'rgb-programmable'
    ],
    'neon-signs': [
        'custom-neon',
        'neon-lamps'
    ],
    'light-boxes': [
        'slim',
        'blade',
        'fabric'
    ],
    'logo-signs': [
        'metal-acrylic'
    ],
    'factory': [
        'production',
        'facilities'
    ],
    'portfolio': [
        'retail',
        'restaurant',
        'hotel',
        'corporate'
    ],
    'general': [
        'hero',
        'icons',
        'misc'
    ]
}

# Create folders
for main_folder, subfolders in folder_structure.items():
    main_path = os.path.join(base_path, main_folder)
    
    # Create main folder if it doesn't exist
    if not os.path.exists(main_path):
        os.makedirs(main_path)
        print(f'Created: {main_folder}/')
    
    # Create subfolders
    for subfolder in subfolders:
        sub_path = os.path.join(main_path, subfolder)
        if not os.path.exists(sub_path):
            os.makedirs(sub_path)
            print(f'Created: {main_folder}/{subfolder}/')
        
        # Create .gitkeep file
        gitkeep_path = os.path.join(sub_path, '.gitkeep')
        if not os.path.exists(gitkeep_path):
            with open(gitkeep_path, 'w') as f:
                f.write('')
            print(f'Created: {main_folder}/{subfolder}/.gitkeep')

print('\nFolder structure created successfully!')
