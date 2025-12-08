"""
Image utility to randomly select images from static/images folders
"""
import os
import glob
import random


class ImageSelector:
    """Select random images from organized image folders"""
    
    BASE_PATH = 'static/images'
    
    # Map category slugs to folder paths
    CATEGORY_MAP = {
        # Channel Letters
        'front-lit': 'channel-letters/front-lit',
        'back-lit': 'channel-letters/back-lit',
        'front-back-lit': 'channel-letters/front-back-lit',
        'open-face': 'channel-letters/open-face',
        'non-illuminated': 'channel-letters/non-illuminated',
        'rgb-programmable': 'channel-letters/rgb-programmable',
        
        # Neon Signs  
        'custom-neon': 'neon-signs',
        'neon-lamps': 'neon-signs',
        
        # Light Boxes
        'slim-lightboxes': 'light-boxes',
        'blade-lightboxes': 'light-boxes',
        'fabric-lightboxes': 'light-boxes',
        
        # Other
        'logo-signs': 'logo-signs',
    }
    
    @classmethod
    def get_images_for_category(cls, category_slug, count=6, prefer_watermark_free=True):
        """
        Get random images for a category
        
        Args:
            category_slug: Category slug (e.g., 'front-lit', 'back-lit')
            count: Number of images to return
            prefer_watermark_free: Prefer images from '无水印' folders
            
        Returns:
            List of image paths relative to static/
        """
        folder_path = cls.CATEGORY_MAP.get(category_slug)
        if not folder_path:
            return []
        
        full_path = os.path.join(cls.BASE_PATH, folder_path)
        
        # Get all image files
        extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
        all_images = []
        
        for ext in extensions:
            pattern = os.path.join(full_path, '**', ext)
            all_images.extend(glob.glob(pattern, recursive=True))
        
        if not all_images:
            return []
        
        #  Prefer watermark-free images
        if prefer_watermark_free:
            watermark_free = [img for img in all_images if '无水印' in img or 'LOGO版' not in img]
            if watermark_free:
                all_images = watermark_free
        
        # Randomly select images
        selected = random.sample(all_images, min(count, len(all_images)))
        
        # Convert to web paths (relative to static/)
        web_paths = []
        for img_path in selected:
            # Convert Windows path to web path
            rel_path = os.path.relpath(img_path, 'static')
            web_path = 'images/' + rel_path.replace('\\', '/')
            web_paths.append(web_path)
        
        return web_paths
    
    @classmethod
    def get_random_images(cls, folder_name, count=6, prefer_watermark_free=True):
        """
        Get random images from a specific folder
        
        Args:
            folder_name: Folder name (e.g., 'channel-letters', 'neon-signs')
            count: Number of images
            prefer_watermark_free: Prefer无水印 fol ders
        """
        full_path = os.path.join(cls.BASE_PATH, folder_name)
        
        extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
        all_images = []
        
        for ext in extensions:
            pattern = os.path.join(full_path, '**', ext)
            all_images.extend(glob.glob(pattern, recursive=True))
        
        if not all_images:
            return []
        
        if prefer_watermark_free:
            watermark_free = [img for img in all_images if '无水印' in img]
            if watermark_free:
                all_images = watermark_free
        
        selected = random.sample(all_images, min(count, len(all_images)))
        
        web_paths = []
        for img_path in selected:
            rel_path = os.path.relpath(img_path, 'static')
            web_path = 'images/' + rel_path.replace('\\', '/')
            web_paths.append(web_path)
        
        return web_paths
