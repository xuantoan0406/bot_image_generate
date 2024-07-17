from diffusers import DiffusionPipeline, EulerAncestralDiscreteScheduler, StableDiffusionXLPipeline
from diffusers import StableDiffusionPipeline
import torch


def image_generate():
    pipe_id = "LahMysteriousSDXL_Lightning.safetensors"
    pipe = StableDiffusionPipeline.from_pretrained(pipe_id, torch_dtype=torch.float16,use_safetensors=True).to("cuda")
    # pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    # pipe.load_lora_weights("nerijs/pixel-art-xl", weight_name="pixel-art-xl.safetensors", adapter_name="pixel")
    # pipe.set_adapters("pixel")

    lora_scale = 0.9
    prompt = "person, Princess, Blazon Card picture composition with a slim frame but without text, ((Fantasy-themed, fantasy art, swift brush strokes)), (Pulp:0.9), ((Dark and grim colors and mood)), embossed in metal (Victorian Gothic Art:1.3),(Dark hue:1.3) stricken background naked Prairie troubled weather John Ruskin, Guido Buzzelli, Abbott Handerson Thayer Pokémon style . vibrant, cute, anime, fantasy, reminiscent of Pokémon series "
    negative_prompt = "((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), out of frame, extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), bad-hands-5"
    width = 512
    height = 512
    num_inference_steps = 10
    guidance_scale = 2
    image = pipe(prompt, negative_prompt=negative_prompt, width=width, height=height, guidance_scale=guidance_scale,
                 num_inference_steps=num_inference_steps).images[0]
    image.save("a.png")


# image_generate()
pipe = StableDiffusionXLPipeline.from_single_file(
    "../../../assets/weight_model/LahMysteriousSDXL_Lightning.safetensors")
pipe.to("cuda")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

# Load the LoRA
# pipe.load_lora_weights('ntc-ai/SDXL-LoRA-slider.anime', weight_name='anime.safetensors', adapter_name="anime")

# Activate the LoRA
pipe.set_adapters(["anime"], adapter_weights=[2.0])

prompt = "person, Princess, Blazon Card picture composition with a slim frame but without text, ((Fantasy-themed, fantasy art, swift brush strokes)), (Pulp:0.9), ((Dark and grim colors and mood)), embossed in metal (Victorian Gothic Art:1.3),(Dark hue:1.3) stricken background naked Prairie troubled weather John Ruskin, Guido Buzzelli, Abbott Handerson Thayer Pokémon style . vibrant, cute, anime, fantasy, reminiscent of Pokémon series "
negative_prompt = "((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), out of frame, extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), bad-hands-5"
width = 640
height = 1280
num_inference_steps = 10
guidance_scale = 2
image = pipe(prompt, negative_prompt=negative_prompt, width=width, height=height, guidance_scale=guidance_scale, num_inference_steps=num_inference_steps).images[0]
image.save('cute.png')
# pipe.set_adapters(["pixel", "toy"], adapter_weights=[0.5, 1.0])
