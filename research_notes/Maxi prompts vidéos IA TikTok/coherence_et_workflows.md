# Consistency techniques and end-to-end workflows for AI story series (fruits/food, animals, cartoons, micro-dramas)

Research date: 2026-10-15. Method note: Reddit (r/aivideo, r/VEO3, r/StableDiffusion, r/comfyui) could not be reached. The search tool refuses reddit.com and direct requests return HTTP 403, so the community practice below comes from blogs, GitHub guides and vendor docs that compile it. License facts for GitHub repos were checked on 2026-10-15 by downloading each repo's own `LICENSE` file from raw.githubusercontent.com. Where a README badge disagrees with that file, both are noted.

## Q1. Which concrete consistency techniques do experienced creators recommend for multi-shot AI stories, and which work best for anthropomorphic characters like fruits?

### Takeaway
Every source converges on the same stack:
1. Lock the cast before animating, using a character bible plus canonical reference images.
2. Paste the same appearance text into every shot prompt, and change only the action, camera and location.
3. Generate a keyframe per shot, then animate it with image-to-video. The alternative is the model's native reference feature: Veo "Ingredients", Sora "Characters"/cameos, Kling "Elements", or Grok multi-ref.
4. Assemble the clips in an editor.

Frame chaining and seeds are secondary aids. Seeds do not guarantee determinism, and chaining accumulates drift. For fruit and other non-human characters, image references matter more than text, because a text description cannot pin down one specific fruit face. Sora and Kling both explicitly support animals, objects and CG characters as reusable characters.

### Cited Findings

**Model-native reference features (official docs)**
- **Veo 3.1 "Ingredients to Video":** you provide "reference images of a scene, character, object, or style to maintain a consistent aesthetic across multiple shots. This feature now includes audio generation." Google's workflow creates the reference images first with Gemini 2.5 Flash Image ("Nano Banana"), then refers to them by role in each shot prompt. Its example: *"Using the provided images for the detective, the woman, and the office setting, create a medium shot of the detective behind his desk. He looks up at the woman and says in a weary voice, "Of all the offices in this town, you had to walk into mine.""* The second shot repeats the same opening clause verbatim — [Google Cloud, Ultimate prompting guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- **Veo 3.1 first and last frame:** generates "a natural video transition between a provided start image and end image, complete with audio". Both frames are made beforehand in Gemini 2.5 Flash Image — [Google Cloud guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- **Veo 3.1 timestamp prompting:** several shots in one 8 s generation, written as `[00:00-00:02] Medium shot ... [00:02-00:04] Reverse shot ...`. The character is re-described inside each segment, e.g. "a young female explorer with a leather satchel and messy brown hair in a ponytail" — [Google Cloud guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- **Veo 3.1 API limits:**
  - Up to **3 reference images**, which help "preserve the subject's appearance". Reference images force an 8 s duration and are not available on Veo 3.1 Lite.
  - `lastFrame` must be used together with `image`, which sets the first frame.
  - Extension adds **7 s, up to 20 times**, and is built from the **final second (24 frames)** of the input video, for up to 148 s total.
  - `seed` "doesn't guarantee determinism, but slightly improves it".
  - Durations are 4, 6 or 8 s, in 16:9 or 9:16.
  - Source: [Gemini API, Veo docs](https://ai.google.dev/gemini-api/docs/veo)
- **Sora 2 Characters API:**
  - Endpoint `POST /v1/videos/characters` creates a reusable character from an MP4 clip of 2–4 s, 720p–1080p, in 16:9 or 9:16.
  - "You can create characters out of any animals or objects."
  - "We recommend no more than 2 characters per generation." Up to two character IDs per request; "include the character ID and refer to the character by name in the prompt."
  - The `input_reference` image anchors the first frame and must match the output resolution.
  - Source: [OpenAI Sora 2 Prompting Guide (cookbook)](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)
- **Sora 2 prompting advice:** "Keep descriptions consistent across shots, reuse phrasing for continuity, and avoid mixing traits that may compete." With new characters, "small changes in phrasing can alter identity, pose, or the focus of the scene itself." Multi-shot prompts are allowed if you "keep each shot block distinct: one camera setup, one subject action, and one lighting recipe at a time." — [OpenAI cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)
- **Sora app "character cameos" (Oct. 2025):** reusable characters made from an uploaded video of a pet, toy, object or original persona, then tagged in later generations. The same update added video stitching — [MacRumors](https://www.macrumors.com/2025/10/30/openai-sora-app-character-cameos-video-stitching/); [Engadget](https://www.engadget.com/ai/openais-character-cameos-will-let-you-put-pets-and-original-personas-in-sora-videos-123043189.html) (Engadget: a few seconds of footage is enough, and older Sora videos can serve as the reference).
- **Kling Elements (Element Library 3.0):**
  - An element needs "at least 2 reference images (1 main reference image + 1 additional reference image)", up to 4 in total, and a front-facing main image is recommended. Kling O1 Image can generate the extra views from one image.
  - A video character element takes a 3–8 s clip.
  - Per generation: Video 3.0 Omni/O1 takes up to 7 images or elements without a video input, and 4 with one. In Video 3.0 with a start frame (or start and end frames), you can bind up to 3 extra elements, and they must appear in the reference frames.
  - Prompts reference elements with "@", e.g. `[@Banana Cat]`, and shots are labelled `[Shot 1]`, `[Shot 2]`.
  - Supported element types include realistic, anime-style and CG-rendered animals and characters, props, costumes and scenes.
  - Source: [Kling Element Library user guide](https://kling.ai/quickstart/klingai-element-library-3-user-guide)
- **Kling 3.0 multi-shot:** up to 6 cuts per generation and clips up to 15 s, according to third-party guides — [Higgsfield](https://higgsfield.ai/kling-3.0); [Morphic](https://morphic.com/resources/how-to/kling-3.0-guide). Not checked against Kling's official docs.
- **Grok Imagine:** a tutorial says you can attach named reference images, each locking one thing (a face, a location or a prop). It advises writing a bible and generating references before any video, using references for identity and text for action, and warns: "your character will not look the same in shot 4 as in shot 1 unless you force it with reference images and repeated text" — [YouMind, Grok Imagine filmmaking guide](https://youmind.com/landing/x-viral-articles/grok-imagine-ai-filmmaking-guide). Sources disagree on the reference cap: "up to 7" vs "2-5" — [SelfieLab](https://selfielabstudio.com/blog/grok-imagine-multi-ref-character-workflow-guide-20260311); [Livepeer ref2v example](https://agent.livepeer.org/chapters/seven-reference-cast-reel-example.html).

**Creator and blog techniques (general)**
- **One identity sentence, unchanged:** "Write one sentence that names age, hair, outfit and one distinguishing detail" and paste it unchanged into every prompt. Change only the action, camera and location. If a shot drifts, go back to the original source image or first frame instead of feeding the drifted render back in. Test two adjoining shots before producing a whole scene — [UlazAI, Veo 3 character consistency](https://ulazai.com/character-consistency/)
- **No "memory" between prompts:** asking Veo to "use the same characters as the last scene" doesn't work, so the full description must be repeated — [Tom's Guide](https://www.tomsguide.com/ai/i-turned-my-chaotic-family-life-into-a-sitcom-with-veo-3-heres-what-worked-and-what-didnt)
- **Continuity table:** keep a table of character, wardrobe, props, lens and lighting, and repeat it across shots — [Sider blog on Veo 3.1](https://sider.ai/blog/ai-tools/how-veo-3_1-maintains-character-scene-consistency-in-ai-video)
- **Character bible / spec sheet first:** covering face, hair, body and age before any scene is generated — [AI Prompt Helper](https://prompt-helper.com/consistent-characters-in-veo-3-your-ultimate-guide-to-flawless-ai-video-scenes/)
- **Higgsfield Multishot tip:** "Use one close-up facial shot and two body/wide shots for optimal consistency." — [AI for Real Life newsletter](https://ai-for-real-life.beehiiv.com/p/the-secret-to-consistent-characters-in-veo-3-and-how-to-fix-the-voices-too)

**Fruit-drama specific workflow**

The Flashloop guide below is a vendor blog.
- **Cast:** 5–10 recurring characters with archetypes such as a broccoli matriarch, a grape or eggplant villain, a strawberry or cherry temptress, a banana or corn innocent, and an avocado or pepper heir.
- **Per character:** one master reference prompt covering proportions, clothing, accessories and expression range, plus a signature item (pearls, red lipstick, a gold watch) as a visual anchor. Generate 5–10 reference images in different poses and pick the canonical ones.
- **Per scene:** generate 3–5 image variations and pick the best, then animate 3–5 s clips with image-to-video.
- **Episodes:** 4–6 scenes, 1–2 minutes.
- **Voice and edit:** narration with ElevenLabs or PlayHT, then edit in CapCut with subtitles.
- Source: [Flashloop, How to make AI fruit drama videos](https://www.flashloop.ai/blog/how-to-make-ai-fruit-drama-videos)

All-in-one fruit tools sell "locked" casts. These are vendor claims:
- Dzine's "Consistent Character" locks facial features, clothing and proportions per fruit character — [Dzine](https://www.dzine.ai/tools/ai-fruit-love-island-video-generator/)
- Revid gives each character "a locked visual reference and a dedicated voice", saved to a cast that persists across episodes — [Revid fruit drama generator](https://www.revid.ai/tools/fruit-drama-generator)

Other guides on the fruit-story trend: [Tryzyvo](https://www.tryzyvo.com/blog/what-is-ai-fruit-story); [AICut](https://www.aicut.pro/blog/how-to-make-viral-ai-fruit-story-videos); [MuleRun micro-dramas 2026](https://blog.mulerun.com/p/how-to-make-ai-micro-dramas-for-tiktok-and-reels-2026). Only search snippets were seen for these, not full pages.

**Open-source / local consistency building blocks**
- **StoryDiffusion "Consistent Self-Attention":** "hot-pluggable and compatible with all SD1.5 and SDXL-based image diffusion models". It needs at least 3 prompts; 5–6 are recommended. A motion predictor then turns the consistent images into video. License: Apache-2.0 (LICENSE file verified) — [StoryDiffusion GitHub](https://github.com/HVision-NKU/StoryDiffusion)
- **Wan 2.2 first-to-last-frame (ComfyUI):** the Wan2.2 Fun Inp workflow interpolates between a start and an end image. Its defaults are 576×1024 vertical and about 3–4 s at 24 fps, with a Lightning 4-step LoRA for previews — [RunComfy Wan2.2 Fun Inp](https://www.runcomfy.com/comfyui-workflows/comfyui-wan2-2-fun-inp-workflow-first-to-last-frame-interpolation). Wan 2.2 is Apache-2.0 (LICENSE.txt verified) — [Wan2.2 GitHub](https://github.com/Wan-Video/Wan2.2)
- **Character LoRA on Wan 2.2 14B:** apply the LoRA to both the high-noise and the low-noise experts, place it after the lightx2v LoRA and before ModelSamplingSD3, at strength around 0.5–0.7. This is community guidance — [OreateAI](https://discover.oreateai.com/discover/how-to-set-up-a-wan22-lora-workflow-in-comfyui-for-better-video). LoRA training tool: ostris ai-toolkit, MIT (verified) — [ai-toolkit](https://github.com/ostris/ai-toolkit)
- **Long-video chaining:** the "Wan Video Extender" node extends a video in loops using a VACE control latent. Each loop can take its own prompt and LoRA, it accepts a character reference image, and the author recommends a 16–24-frame overlap — [comfy.icu Wan-video-extender](https://comfy.icu/extension/Granddyser__wan-video-extender)
- **Qwen-Image-Edit 2509:** takes 1–3 input images (person+person, person+product, person+scene) with better identity preservation, and is used to build character-consistent LoRA datasets. The 2511 version is said to improve multi-character consistency — [RunComfy Qwen Image Edit 2509](https://www.runcomfy.com/comfyui-workflows/qwen-image-edit-2509-in-comfyui-multi-image-merge-edit); [WeirdWonderfulAI LoRA dataset](https://weirdwonderfulai.art/comfyui/qwen-image-edit-can-create-character-consistent-lora-dataset/); [StableDiffusionTutorials](https://www.stablediffusiontutorials.com/2025/09/qwen-image-edit-2509.html). Qwen-Image repo is Apache-2.0 (verified) — [Qwen-Image GitHub](https://github.com/QwenLM/Qwen-Image)

### Inferences
- **Typical end-to-end workflow** (synthesis of Google, Flashloop, ViMax, huobao, drama-skills and VideoClaw):
  1. Story or idea to an episode script, written by an LLM.
  2. A character, setting and prop bible with fixed text blocks.
  3. Reference sheets: front view plus 1–3 other angles per character, plus one image per recurring set.
  4. A shot list or storyboard, each shot with camera, action, dialogue, start state and end state.
  5. A keyframe image per shot, made from the references with an image-edit model.
  6. Image-to-video, or reference-to-video, per shot.
  7. Voice: native, or TTS/voice conversion plus lip-sync.
  8. Assembly in an editor or FFmpeg, adding music, subtitles and a cliffhanger card.
- **Where the "maxi prompt" fits:** it is the per-shot prompt assembled from fixed blocks plus one variable block. Suggested skeleton: `[STYLE BLOCK – identical every shot] + [CHARACTER BLOCK(S) – pasted verbatim, one per character in frame] + [SETTING BLOCK – identical per location] + [SHOT: camera + action + emotion – variable] + [DIALOGUE with speaker identified by visual descriptor + VOICE BLOCK – fixed per character] + [AUDIO ambience] + [NEGATIVES: no subtitles/no on-screen text/no extra characters]`. Each part is attested separately:
  - Flashloop's identical style suffix
  - drama-skills' "lock phrase pasted unchanged"
  - UlazAI's identity sentence
  - huobao's visual style "injected into every image prompt"
  - snubroot's negatives
- **Which method for fruits:** reference-based features (Kling Elements, Sora Characters, Veo Ingredients, Grok multi-ref) plus one signature accessory per character are the most robust choice. Text alone cannot uniquely describe a cartoon fruit face. Sora and Kling explicitly accept objects, animals and CG characters as references.
- **Frame chaining** (last frame becomes the next first frame) is best kept for continuous action inside one scene. Between scenes, restart from the canonical references, per UlazAI's "return to the original source image" rule and the fact that Veo extension is built only from the last 24 frames.

### Gaps
- No Reddit thread could be read directly, so verbatim r/aivideo and r/VEO3 tips are missing. YouTube tutorial transcripts were not retrieved.
- No source measured whether frame chaining or reference images is better for fruit characters specifically.
- Kling 3.0's multi-shot limits (6 cuts / 15 s) come from third parties and were not confirmed in official docs.

## Q2. How do creators write a reusable character description block (attributes, length, exact repetition, naming vs describing)? Verbatim examples.

### Takeaway
The dominant pattern is one dense sentence or JSON object per character, pasted verbatim into every shot. It covers species or age, body shape, colors, outfit, one distinguishing detail or signature accessory, posture, and optionally a voice and demeanor. Any word change, even adding "wearing glasses", is reported to break identity.

Names alone do not work on Veo-type models: the model "doesn't know" names. Names do work once a character is registered as a reference: Sora character ID, Kling `@element`, huobao `@character`. No source gives an optimal word count.

### Cited Findings

**Template examples (verbatim)**
- **Veo 3 community guide**, template: `[NAME], a [AGE] [ETHNICITY] [GENDER] with [SPECIFIC_HAIR_DETAILS], [EYE_COLOR] eyes, [DISTINCTIVE_FACIAL_FEATURES], wearing [DETAILED_CLOTHING_DESCRIPTION], with [POSTURE_AND_MANNERISMS]`. Example: *"Sarah Chen, a 32-year-old Asian-American woman with shoulder-length black hair styled in a professional bob, warm brown eyes behind wire-rimmed glasses, wearing a charcoal gray blazer over a white collared shirt, with confident posture and an approachable smile that creates small crinkles around her eyes."* That example is about 50 words. Source: [snubroot/Veo-3-Prompting-Guide](https://github.com/snubroot/Veo-3-Prompting-Guide). No LICENSE file was found in the repo.
- **Same guide, outfit change across scenes:** scene 2 reuses the face words and swaps the clothes explicitly: *"Dr. Jennifer Walsh, the same 35-year-old pediatrician with short brown hair in a bob cut and kind green eyes, now wearing a casual green sweater and dark jeans..."* — [snubroot guide](https://github.com/snubroot/Veo-3-Prompting-Guide)
- **Same guide, signature elements and behavior blocks:** *"The detective always wears his vintage leather jacket, silver watch on his left wrist, and carries a worn brown leather notebook. These signature elements appear in every scene."* and *"The professor has a habit of adjusting his glasses when thinking deeply..."* — [snubroot guide](https://github.com/snubroot/Veo-3-Prompting-Guide)
- **Short identity sentence:** *"A 7-year-old with curly red hair, yellow raincoat, one front tooth missing"* must "read exactly the same in each clip". Put the voice in the same block, e.g. *"quiet, high-pitched, slightly hoarse"*, and add one demeanor note such as *"cautious, observant"* — [UlazAI](https://ulazai.com/character-consistency/)
- **Exact repetition test ($400 of tests):** "realistic bigfoot" stays consistent across prompts, while "realistic bigfoot wearing glasses" breaks it, so even small additions alter the character — [Alejandro Dinsmore, Deep Dive Veo 3](https://alejandrodinsmore.substack.com/p/deep-dive-veo-3-i-spent-400-testing)
- **JSON character block:** excerpts such as `"skin_tone": "warm beige with sun-kissed undertones"`, `"color": "chestnut brown with caramel highlights"`, `"top": "cream silk camisole"`, `"outerwear": "lightweight, oversized camel trench coat, belt loosely tied at back"`, `"footwear": "tan leather ankle boots, slightly scuffed at toes"`. Later clips keep the block and change only the scene. In a Gemini chat, the follow-up was simply "Create a video of the same girl driving a sports car" — [AI for Real Life](https://ai-for-real-life.beehiiv.com/p/the-secret-to-consistent-characters-in-veo-3-and-how-to-fix-the-voices-too)

**Fruit prompts and naming**
- Shot prompts describe the fruits by visual details, never by name: *"An elderly broccoli woman in a silk ivory robe and pearl necklace stands pointing accusingly at a tall grape man"*; *"A broccoli man in a gray suit leans across the table toward a cherry woman in a red dress"*; *"a young strawberry woman in a cream silk dress, standing in an elegant marble bathroom"*.
- Every prompt ends with the same style suffix: *"3D animated style, photorealistic, cinematic composition, 9:16 vertical."*
- Motion prompt example: *"The character turns slowly to face camera, expression shifts from smile to shock"*.
- The guide's reasoning: refer to characters by visual description, not name, "because the AI doesn't know character names".
- Source: [Flashloop](https://www.flashloop.ai/blog/how-to-make-ai-fruit-drama-videos)

**"Continuity lock" pattern (open-source drama-skills, MIT)**
- A look that must hold across shots is written as one phrase "pasted into every affected prompt unchanged". Example: *"Continuity lock: LOCK-JIANGCHEN-DRESS "Jiang Chen's pine-green service uniform" (shots: SHOT-EP001-002, SHOT-EP001-003, SHOT-EP001-007, …; image prompt entry: IMG-JIANGCHEN-SHEET) · lock phrase: pine-green lapel service jacket"*.
- The keyframe prompt embeds the lock phrase and ends with *"no text, no logo."*
- The video prompt describes only the actions between the start and end frames.
- A checker script verifies the declared locks.
- Source: [zenstory-ai/drama-skills README](https://github.com/zenstory-ai/drama-skills/blob/main/README_EN.md)

**Naming once a reference is registered**
- Sora: "include the character ID and refer to the character by name in the prompt" — [OpenAI cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)
- Kling: `@` syntax such as `[@Banana Cat]` — [Kling guide](https://kling.ai/quickstart/klingai-element-library-3-user-guide)
- huobao-drama: "`@character` references map to reference images automatically" — [huobao-drama](https://github.com/chatfire-AI/huobao-drama)
- Veo Ingredients: refer by role, "the provided images for the detective, the woman, and the office setting" — [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)

**Multi-character dialogue: identify speakers by a visual tag**
- *"The woman in the red dress asks: ... The man in the blue shirt replies: ..."* — [snubroot guide](https://github.com/snubroot/Veo-3-Prompting-Guide)
- Sora: "label speakers consistently and use alternating turns" — [OpenAI cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)

### Inferences
- **A fruit character block would list:** fruit species and exact color and texture; body shape and size relative to the others; face (eye style and color, brows, mouth); limbs (cartoon arms and legs or none); outfit and accessories with one signature item; posture or mannerism; and, for native-audio models, a fixed voice line (age, gender, pitch, accent, tempo, timbre).
- **Recommended length:** keep it to one sentence or one compact JSON object, roughly 30–60 words, which matches the published examples. No source tested an optimal length.
- **When to name the character:** give it a name for the human team and the bible, but put the description in the prompt unless the platform has a registered character or element.

### Gaps
- No source quantifies the ideal word count or compares JSON with prose blocks.
- No verbatim fruit character block covering face, voice and outfit was found. Flashloop describes a "master reference prompt" but does not show one.

## Q3. Which free/open-source pipelines on GitHub automate story → shot list → prompts → images → video? License, and do they work with free models?

### Takeaway
Many permissively licensed orchestrators now exist: ViMax (MIT), Toonflow (MIT), drama-skills (MIT), VideoClaw/FilmAgent (MIT), Jellyfish (Apache-2.0) and AIDrama Studio (Apache-2.0 LICENSE file, MIT badge). Nearly all of them call paid APIs by default: Veo, Nano Banana, Seedance, Kling, MiniMax or FLUX through aggregators.

Truly free and local pipelines rely on research code (MovieAgent with HunyuanVideo-I2V and StoryDiffusion) or on Toonflow's ComfyUI connector paired with open weights such as Wan 2.2 and Qwen-Image (both Apache-2.0). huobao-drama and HoloCine are non-commercial (CC BY-NC-SA 4.0).

### Cited Findings

**Orchestrators**
- **ViMax (HKUDS):**
  - Modes: Idea2Video, Script2Video and Novel2Video, plus AutoCameo (puts a person or pet from a photo into stories).
  - Stages: scriptwriting, storyboarding, character creation and video generation. It coordinates "references, first frames, camera continuity, and final assembly" and generates 2 keyframe candidates, then picks one with a vision model (`num_candidates: 2`).
  - Default config: LLM `google/gemini-2.5-flash-lite` through OpenRouter, images `ImageGeneratorNanobananaGoogleAPI`, video `VideoGeneratorVeoGoogleAPI`. Newer support covers GPT Image 2, Seedance 2.0 Fast and MiniMax.
  - Stats: 12.7k stars, v1.2.0 released 2026-07-20.
  - License: MIT (verified).
  - Free/local model support is not documented; every example needs an API key.
  - Sources: [ViMax GitHub](https://github.com/HKUDS/ViMax); paper [arXiv 2606.07649](https://arxiv.org/html/2606.07649v1). The paper reports ViMax with Veo 3.1 scoring Overall GC 0.5571, vs HoloCine 0.5272, MovieAgent 0.4716 and AniMaker 0.5167.
- **MovieAgent (showlab):**
  - Multi-agent chain-of-thought planning with director, screenwriter, storyboard and location-manager roles.
  - Inputs: a script synopsis plus a "photo,audio of character" folder per character.
  - Uses StoryDiffusion and ROICtrl for character customization and HunyuanVideo-I2V, downloaded locally, so it runs on local GPUs.
  - No LICENSE file was found at the repo root.
  - Sources: [MovieAgent GitHub](https://github.com/showlab/MovieAgent); [project page](https://weijiawu.github.io/MovieAgent/)
- **StoryDiffusion:** consistent-image generation for SD1.5/SDXL, plus image-to-video. Apache-2.0 (verified) — [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion)
- **huobao-drama (火宝短剧):**
  - Pipeline: one sentence → script → extract characters, scenes and props → a consistent reference image for each, "injected as reference material when generating videos" → storyboard breakdown with video prompts (`@character` mapped to the references) → per-shot video → FFmpeg merge.
  - The visual style chosen at project creation is "injected into every image prompt".
  - Video models: Seedance 2.0, MiniMax H3 and Wan 3.0, all through paid APIs.
  - License: **CC BY-NC-SA 4.0**, so no commercial use without permission (LICENSE verified).
  - Source: [huobao-drama GitHub](https://github.com/chatfire-AI/huobao-drama)
- **AIDrama Studio (EvoLinkAI/ai-short-drama):**
  - Pipeline: novel → script analysis → storyboard → images → videos → voiceover → final drama.
  - A "Character Workshop" keeps the "same face, same outfit".
  - Per-character voices with lip-synced dialogue, using CosyVoice TTS.
  - Needs one EvoLink API key, a paid aggregator.
  - License: the README says MIT, but the LICENSE file is **Apache-2.0**. Both allow commercial use.
  - Source: [EvoLinkAI/ai-short-drama](https://github.com/EvoLinkAI/ai-short-drama)
- **Jellyfish (Forget-C):** a production workspace that treats "consistency as a first-class problem". It centrally manages characters, scenes, props and costumes, keyframes and reference images, and video prompts. Apache-2.0 (verified) — [Jellyfish GitHub](https://github.com/Forget-C/Jellyfish)
- **Open-AI-Micro-Drama-Generator (Anil-matcha):**
  - Pipeline: Claude Sonnet through MuAPI → character extraction with "static + dynamic features" → `flux-dev-image` portrait per character → `flux-kontext-dev-i2i` first frame per shot using the character references → `kling-v2.1-standard-i2v` 5 s clip → moviepy concatenation.
  - Needs a single paid MuAPI key.
  - The README badge says MIT, but no LICENSE file was found at the root.
  - Source: [Open-AI-Micro-Drama-Generator](https://github.com/Anil-matcha/Open-AI-Micro-Drama-Generator)
- **Toonflow (HBAI-Ltd/Toonflow-app):** a canvas workflow covering characters and scenes, then multi-reference video per shot. It can connect "local ComfyUI and LLM" through a custom provider. License: **MIT** (verified). The README says the project switched from Apache-2.0 to MIT and dropped its commercial add-on terms. This contradicts a blog that calls it AGPL-3.0 ([Apiyi blog](https://help.apiyi.com/en/toonflow-ai-short-drama-comic-tool-api-guide-en.html)). Source: [Toonflow GitHub](https://github.com/HBAI-Ltd/Toonflow-app)
- **drama-skills (zenstory-ai):**
  - 11 agent skills for Claude Code or Codex.
  - Pipeline: source analysis → episode script → visual design → image prompts and storyboard → video prompts → confirmed production → editing → review.
  - Writes plain Markdown files (script, visual design, storyboard, image prompts, video prompts) with continuity locks and a checker, and runs nothing paid without confirmation.
  - License: MIT (verified).
  - Source: [drama-skills](https://github.com/zenstory-ai/drama-skills/blob/main/README_EN.md)
- **VideoClaw (repo HITsz-TMG/FilmAgent):** script planning → character and scene design → storyboard → reference images → video (Wan 2.7 i2v, Seedance 2.0, Kling v3 through DashScope, ARK or Kling keys) → final edit. It also has a "Digital Human Talking Video" mode. License: MIT (verified) — [HITsz-TMG/FilmAgent (VideoClaw)](https://github.com/HITsz-TMG/FilmAgent)
- **HoloCine** (multi-shot holistic video research, used as a ViMax baseline): **CC BY-NC-SA 4.0** (verified), non-commercial — [HoloCine GitHub](https://github.com/yihao-meng/HoloCine)
- **More repos** are listed under the GitHub topics [short-drama](https://github.com/topics/short-drama) and [ai-filmmaking](https://github.com/topics/ai-filmmaking).

**Free/open model building blocks**

All licenses below were read from the repo LICENSE files on 2026-10-15.
- Video: [Wan 2.2](https://github.com/Wan-Video/Wan2.2), Apache-2.0; [LTX-Video](https://github.com/Lightricks/LTX-Video), Apache-2.0
- Images and editing: [Qwen-Image](https://github.com/QwenLM/Qwen-Image), Apache-2.0
- Lip-sync / talking video: [InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk), Apache-2.0; [LatentSync](https://github.com/bytedance/LatentSync), Apache-2.0
- TTS: [Chatterbox](https://github.com/resemble-ai/chatterbox), MIT; [Kokoro](https://github.com/hexgrad/kokoro), Apache-2.0; [IndexTTS](https://github.com/index-tts/index-tts), custom "bilibili Model Use License Agreement" (read it before commercial use)
- Voice conversion: [RVC WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI), MIT; [Seed-VC](https://github.com/Plachtaa/seed-vc), GPL-3.0
- LoRA training: [ostris ai-toolkit](https://github.com/ostris/ai-toolkit), MIT

### Inferences
- **Fully free path:** a free LLM writes the script and shot list (drama-skills-style Markdown files with continuity locks). Then:
  1. Qwen-Image / Qwen-Image-Edit builds the reference sheets and keyframes, optionally with a character LoRA trained in ai-toolkit.
  2. Wan 2.2 i2v or FLF in ComfyUI animates each shot.
  3. Chatterbox or Kokoro TTS voices it, optionally converted to a fixed per-character voice with RVC.
  4. InfiniteTalk or LatentSync adds lip-sync, and FFmpeg assembles the episode.
  - Toonflow or ViMax (configurable `base_url`) could orchestrate this, but neither documents a ready-made local preset.
- **Code license vs weight license:** a code license does not cover model weights. For example, the FLUX.1-dev and Kontext-dev weights used by Anil-matcha's pipeline are commonly reported as non-commercial, which was not verified here.

### Gaps
- Not verified: whether ViMax or AIDrama Studio run end to end with local models (Ollama or ComfyUI) without code changes.
- MovieAgent's license is unknown; no LICENSE file was found.
- Star counts and activity were not obtained for most repos; the GitHub API was not reachable from this session.
- No GitHub project found is specialized in fruit or cartoon talking-object series.

## Q4. How do people keep the same voice per character across clips with native-audio models (Veo 3, Sora 2, Grok Imagine)?

### Takeaway
Three approaches are in use:
- **(a) Fixed voice description pasted into every prompt.** Cheapest, but unreliable. Neither Google nor OpenAI documents any voice-locking control.
- **(b) Platform voice binding.** Kling 3.0 Elements accept a 5–30 s voice sample or a Voice Library voice per character. Grok Imagine reportedly added voice references (unverified).
- **(c) Replace the audio afterwards.** Either convert each clip's dialogue to one cloned voice with speech-to-speech (ElevenLabs Voice Changer, or open-source RVC / Seed-VC), or generate TTS first and lip-sync.

Many fruit-drama channels avoid the problem entirely with a single narrator voice-over.

### Cited Findings
- **Veo:** audio is always on. Dialogue goes in quotation marks, English is "fully supported" and other languages are unevaluated. Voice is only carried into an extension if it occurs in the last second of the clip. No voice-consistency parameter is documented — [Gemini API Veo docs](https://ai.google.dev/gemini-api/docs/veo)
- **Google's own Veo 3.1 example** describes the voice inline ("says in a weary voice"). The guide offers no cross-shot voice technique, though "Ingredients to Video" now "includes audio generation" — [Google Cloud guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- **Sora 2:** the cookbook gives dialogue formatting only ("Dialogue:" block, label speakers consistently, one or two short exchanges per 4 s shot). It has nothing on keeping a voice across clips — [OpenAI cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)
- **Kling 3.0 voice binding:** applies to character elements. Sources are an uploaded "5-30s single-person speaking audio" (clean background, moderate speed, neutral consistent tone), the Voice Library, or the vocal track of a video element; "No Voice" is also an option — [Kling Element Library guide](https://kling.ai/quickstart/klingai-element-library-3-user-guide). Once bound, the voice persists without being re-specified in later prompts — [Morphic](https://morphic.com/resources/how-to/kling-3.0-guide). Third parties disagree on the sample length (3–8 s) — [Atlas Cloud](https://www.atlascloud.ai/blog/tips/solving-character-inconsistency-a-guide-to-kling-3.0-image-to-video-mode)
- **Grok Imagine:** a July 31 update reportedly "added image and voice references". No details on how well they hold — [YouMind](https://youmind.com/landing/x-viral-articles/grok-imagine-ai-filmmaking-guide)
- **Voice in the same fixed block as looks:** e.g. "quiet, high-pitched, slightly hoarse" — [UlazAI](https://ulazai.com/character-consistency/). The character bible should include "vocal tone and speech quirks", with the same language reused every time — [Artlist](https://artlist.io/blog/consistent-character-ai/)
- **Native generation, then normalization:** generate Veo 3 clips with "brief voice and accent descriptions", export the audio to the timeline, and run the clips through the ElevenLabs voice changer "to standardize them to one voice profile" — [AI for Real Life](https://ai-for-real-life.beehiiv.com/p/the-secret-to-consistent-characters-in-veo-3-and-how-to-fix-the-voices-too)
- **ElevenLabs Voice Changer:** speech-to-speech that keeps the original delivery. A listed use case is "consistent character voices across multiple languages and recording sessions". Segments are limited to 5 minutes, billed at 1,000 characters per minute — [ElevenLabs docs](https://elevenlabs.io/docs/overview/capabilities/voice-changer)
  - Treat the output as a new dialogue stem; close-ups are less forgiving for sync — [Seedance.tv tutorial](https://www.seedance.tv/blog/elevenlabs-voice-changer-video-tutorial)
  - Another guide recommends stripping the generated audio and dubbing with a cloned voice, noting Instant Voice Cloning is usually enough for short dialogue — [MindStudio](https://www.mindstudio.ai/blog/elevenlabs-voice-cloning-replace-ai-generated-voices)
- **Fruit-drama voice approach:** use one dramatic narrator voice in ElevenLabs or PlayHT (free tier available), at about 80–90 characters of narration per scene (5–8 s) — [Flashloop](https://www.flashloop.ai/blog/how-to-make-ai-fruit-drama-videos). Revid advertises a "dedicated voice" saved per character in a persistent cast (vendor claim) — [Revid](https://www.revid.ai/tools/fruit-drama-generator)
- **Open-source TTS then lip-sync:** InfiniteTalk (Wan 2.1-based) turns a single character image plus audio into a lip-synced video using wav2vec2 audio features. A multi-person version uses a mask per character. The sources do not confirm results on cartoon or non-human faces — [ComfyUI Wiki InfiniteTalk](https://comfyui-wiki.com/en/models/wan/infinitetalk); [Comfy template](https://comfy.org/templates/templates-wan2_1_infinitetalk_music)
- **Pipelines that separate voice by design:**
  - AIDrama Studio: "Design unique voices for each character, generate lip-synced dialogue" — [EvoLinkAI/ai-short-drama](https://github.com/EvoLinkAI/ai-short-drama)
  - MovieAgent: takes an audio sample per character as input — [MovieAgent](https://github.com/showlab/MovieAgent)

### Inferences
- **Most reliable for a recurring cast of fruits:** either (1) Kling with a voice bound to each element, or (2) any video model, followed by per-character speech-to-speech conversion to a fixed target voice (ElevenLabs, or free RVC / Seed-VC with license caveats). Option (2) keeps the native lip timing because conversion preserves the delivery.
- **Pure prompt description with Veo, Sora or Grok:** use it only with an identical voice line (age, gender, pitch, accent, tempo, timbre), and expect drift between clips.
- **TTS first, then lip-sync:** gives the most control, but requires a lip-sync model that handles stylized faces. That is unverified for fruit faces, so test before committing.

### Gaps
- No measured comparison of voice drift between Veo, Sora and Grok across clips.
- No confirmation that Veo "Ingredients" or Sora Characters carry a voice identity.
- Grok Imagine voice-reference mechanics are undocumented in the sources found.
- No verbatim "voice block" from an experienced fruit-series creator.

## Q5. How do creators handle unwanted burned-in subtitles/text, extra characters, and face/outfit drift?

### Takeaway
**Subtitles:** the community fix for Veo is formatting (dialogue after a colon; some say drop the quotes and apostrophes) plus explicit "no subtitles / no on-screen text" negatives. Cropping or cleaning in post is the fallback. Sources conflict on quotes: Google's docs use quotation marks; Replicate advises against them.

**Extra characters:** cap the characters per shot (Sora recommends at most 2), describe the frame positively, and give a "no background characters/props" line.

**Drift:** fixed verbatim blocks, signature accessories, canonical reference images, regenerating from the original reference instead of the drifted frame, generating several candidates and picking the best (ViMax automates this with a vision model), and continuity checklists (drama-skills checker, Jellyfish asset manager).

### Cited Findings

**Subtitles**
- **Why it happens and the colon fix:** subtitles come from training on videos with baked-in subtitles. Put speech after a colon without quotes, e.g. "A guy says: My name is Ben" — [Replicate, Using and prompting Veo 3](https://replicate.com/blog/using-and-prompting-veo-3)
- **Veo 3 community guide, three methods:**
  1. Colon format (`Character says: "dialogue"`; "KEY: The colon (:) prevents subtitle generation").
  2. Add "(no subtitles)" or "no subtitles, no text overlays".
  3. For stubborn cases: *"No subtitles. No subtitles! No on-screen text whatsoever."*
  - Caveat: the guide's own "works" and "fails" examples both use colon plus quotes, so it is internally inconsistent.
  - Source: [snubroot guide](https://github.com/snubroot/Veo-3-Prompting-Guide)
- **Apostrophes:** avoid them in the speech line — [VidAU](https://www.vidau.ai/veo-3-prompt-no-subtitles/); [Wondershare](https://videoconverter.wondershare.com/ai-video-tips/remove-veo-ai-caption.html)
- **Post-production fallback:** crop the bottom 10–15% of the frame, where Veo places captions — [Yapper](https://yapper.so/articles/remove-veo3-subtitles)
- **Conflict on quotes:** Google's API docs say dialogue goes in quotation marks — [Gemini API Veo docs](https://ai.google.dev/gemini-api/docs/veo) — while Replicate advises no quotes. Google also advises describing exclusions positively: "a desolate landscape with no buildings or roads" instead of "no man-made structures" — [Google Cloud guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- **Keyframe negatives:** drama-skills keyframes end with "no text, no logo." — [drama-skills](https://github.com/zenstory-ai/drama-skills/blob/main/README_EN.md). The Sora cookbook example says "Avoid signage or corporate branding." — [OpenAI cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)

**Audio hallucinations**
- Always specify the ambience, e.g. *"Audio: quiet office ambiance, no audience sounds, professional atmosphere."*, to avoid an unwanted laugh track — [snubroot guide](https://github.com/snubroot/Veo-3-Prompting-Guide)

**Extra characters and props**
- Lines such as "No background distractions" and "No dialogue, text, or extra props" — [Dinsmore](https://alejandrodinsmore.substack.com/p/deep-dive-veo-3-i-spent-400-testing)
- Sora: "no more than 2 characters per generation", and one subject action per shot block — [OpenAI cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)
- Kling: extra bound elements "must appear in the reference frames" — [Kling guide](https://kling.ai/quickstart/klingai-element-library-3-user-guide)

**Face and outfit drift**
- **Outfit wording:** if the outfit wording changes, "the model follows the newer instruction". Never feed a drifted render back in; go back to the source image — [UlazAI](https://ulazai.com/character-consistency/)
- **Signature items:** pearls, red lipstick or a gold watch as anchors, 5–10 reference poses with one canonical choice, and 3–5 variations per scene — [Flashloop](https://www.flashloop.ai/blog/how-to-make-ai-fruit-drama-videos)
- **Automated selection:** ViMax generates 2 keyframe candidates and picks one with a vision-language model — [ViMax](https://github.com/HKUDS/ViMax)
- **Checklists and tracking:**
  - drama-skills' checker verifies declared references and continuity locks — [drama-skills](https://github.com/zenstory-ai/drama-skills/blob/main/README_EN.md)
  - Jellyfish centralizes character, scene, prop and costume management "to reduce drift across shots" — [Jellyfish](https://github.com/Forget-C/Jellyfish)
  - A continuity table of character, wardrobe, props, lens and lighting — [Sider](https://sider.ai/blog/ai-tools/how-veo-3_1-maintains-character-scene-consistency-in-ai-video)
- **Reference sheets can add unwanted backgrounds:** one creator found Gemini made usable full-body stills for a character sheet but added backgrounds even when told not to — [Winterspeak](https://winterspeak.substack.com/p/veo-3-probably-solves-the-character)
- **Reference image hygiene:** use clean images showing face, shape and key details, and the same references for face, hair, clothing and accessories. References reduce drift but do not guarantee identity — [UlazAI](https://ulazai.com/character-consistency/)

### Inferences
- **Standard negative tail for the maxi prompt:** something like "no subtitles, no captions, no on-screen text, no logos, no other characters in frame, audio: [ambience], no music unless specified". Keep it with colon-style dialogue, and budget a crop or inpaint pass for the remaining failures.
- **Detecting fruit drift:** since fruit faces are simple shapes, color and accessory drift (wrong leaf, missing accessory) is the most visible failure. One signature accessory per character, written identically in both the bible and every prompt, is the cheapest guard.

### Gaps
- No quantitative data on how often each subtitle-prevention method works.
- Nothing found specific to Sora 2 or Grok Imagine burned-in captions.
- No Reddit primary threads could be accessed to confirm the colon/quote debate.
