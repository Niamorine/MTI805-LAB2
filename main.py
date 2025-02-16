import sys
import subprocess
from time import time

script_path = "./stitching_detailed.py"

def stitch(
    img_names: list[str],
    features: str = 'orb',
    matcher: str = 'homography',
    estimator: str = 'homography',
    match_conf: float = 0.3,
    conf_thresh: float = 1.0,
    ba: str = 'ray',
    wave_correct: str = 'horiz',
    warp: str = 'spherical',
    seam_megapix: float = 0.1,
    seam: str = 'gc_color',
    compose_megapix: float = -1,
    expos_comp: str = 'gain_blocks',
    blend: str = 'multiband',
    blend_strength: float = 5,
    output: str = 'result.jpg',
    timelapse: str = None,
    save_graph: str = None,
    ):
    cmd = [sys.executable, script_path] + img_names

    options = {
        '--features': features,
        '--matcher': matcher,
        '--estimator': estimator,
        '--match_conf': match_conf,
        '--conf_thresh': conf_thresh,
        '--ba': ba,
        '--wave_correct': wave_correct,
        '--warp': warp,
        '--seam_megapix': seam_megapix,
        '--seam': seam,
        '--compose_megapix': compose_megapix,
        '--expos_comp': expos_comp,
        '--blend': blend,
        '--blend_strength': blend_strength,
        '--output': output,
    }
    
    if timelapse:
        options['--timelapse'] = timelapse

    for option, value in options.items():
        if value is not None:
            cmd += [option, str(value)]

    # if timelapse:
    #     cmd += ['--timelapse']

    subprocess.run(cmd)


def main():
    
    t_begin = time()
    
    kwargs = {'features': 'sift', 'warp': 'spherical'}
    
    # In theory, the easiest example since the image was just cut in half
    stitch(['assets/east_block_cut1.jpg', 'assets/east_block_cut2.jpg'], **kwargs, output='results/east_block_result.jpg')
        
    # Rotation from the same point
    stitch(['assets/louvre1.jpg', 'assets/louvre2.jpg', 'assets/louvre3.jpg'], **kwargs, output='results/louvre_result.jpg')
    
    # Rotation from the same point, at night
    stitch(['assets/vieux_port2.jpg', 'assets/vieux_port3.jpg'], **kwargs, output='results/vieux_port_result.jpg')
    
    # Rotation from the same point, on image dezoomed
    stitch(['assets/rideau1.jpg', 'assets/rideau2.jpg', 'assets/rideau3.jpg'], **kwargs, output='results/rideau_result.jpg')
    
    stitch(['assets/vue_mtl1.jpg', 'assets/vue_mtl2.jpg', 'assets/vue_mtl3.jpg', 'assets/vue_mtl4.jpg', 'assets/vue_mtl5.jpg'], **kwargs, output='results/vue_mtl_result.jpg')
    
    
    # Genshin, simple, can't stitch with img3
    stitch(['assets/inazuma1.png', 'assets/inazuma2.png', 'assets/inazuma3.png'], **kwargs, output='results/inazuma_result.jpg')

    # Genshin Impact, missing character from img4
    stitch(['assets/fontaine1.png', 'assets/fontaine2.png', 'assets/fontaine3.png', 'assets/fontaine4.png', 'assets/fontaine5.png', 'assets/fontaine6.png'], **kwargs, output='results/fontaine_result.jpg') 

    # Genshin, 8 images stitched !
    stitch(['assets/liyue1.png', 'assets/liyue2.png', 'assets/liyue3.png', 'assets/liyue4.png', 'assets/liyue5.png', 'assets/liyue6.png', 'assets/liyue7.png', 'assets/liyue8.png'], **kwargs, output='results/liyue_result.jpg')
    
    
    t_end = time()
    
    print(f"Execution time: {t_end - t_begin} seconds")

if __name__ == '__main__':
    main()
