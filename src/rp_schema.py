INPUT_SCHEMA = {
    'prompt': {
        'type': str,
        'required': True
    },
    'negative_prompt': {
        'type': str,
        'required': False,
        'default': None
    },
    'width': {
        'type': int,
        'required': False,
        'default': 768,
        'constraints': lambda width: 128 <= width <= 1080
    },
    'height': {
        'type': int,
        'required': False,
        'default': 432,
        'constraints': lambda height: 128 <= width <= 1080
    },
    'prompt_strength': {
        'type': float,
        'required': False,
        'default': 0.8,
        'constraints': lambda prompt_strength: 0 <= prompt_strength <= 1
    },
    'num_outputs': {
        'type': int,
        'required': False,
        'default': 1,
        'constraints': lambda num_outputs: 10 >= num_outputs > 0
    },
    'num_inference_steps': {
        'type': int,
        'required': False,
        'default': 30,
        'constraints': lambda num_inference_steps: 0 < num_inference_steps < 500
    },
    'guidance_scale': {
        'type': float,
        'required': False,
        'default': 7.5,
        'constraints': lambda guidance_scale: 0 < guidance_scale < 20
    },
    'noise_strength': {
        'type': float,
        'required': False,
        'default': 0.35,
        'constraints': lambda noise_strength: 0 < noise_strength < 1
    },
    'scheduler': {
        'type': str,
        'required': False,
        'default': 'DDIM',
        'constraints': lambda scheduler: scheduler in ['DDIM', 'K_EULER', 'DPMSolverMultistep', 'K_EULER_ANCESTRAL', 'PNDM', 'KLMS']
    },
    'seed': {
        'type': int,
        'required': False,
        'default': None
    },
    'nsfw': {
        'type': bool,
        'required': False,
        'default': False
    }
}
