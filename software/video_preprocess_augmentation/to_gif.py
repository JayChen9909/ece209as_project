sample_video = load_video(video_path)[:100]
sample_video.shape
(100, 224, 224, 3) # shape of  the sample video
def to_gif(images):
    converted_images = np.clip(images * 255, 0, 255).astype(np.uint8)
    imageio.mimsave('./data/animation2.gif', converted_images,  fps=25)
    return embed.embed_file('./data/animation2.gif')