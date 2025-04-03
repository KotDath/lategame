class AnimationController():
    def __init__(self, images_dir, max_frame_count, interval):
        self.animation_frame = 1
        self.max_frame_count = max_frame_count
        self.interval = interval
        self.images_dir = images_dir
        self.current_frame = f"{images_dir}/output_001.png"
        
    def next_frame(self, a, b, c):
        if self.animation_frame < self.max_frame_count:
            self.animation_frame += 1
            self.current_frame = f"{self.images_dir}/output_{self.animation_frame:03d}.png"
        else:
            self.animation_frame = 1
            self.current_frame = f"{self.images_dir}/output_{self.animation_frame:03d}.png"