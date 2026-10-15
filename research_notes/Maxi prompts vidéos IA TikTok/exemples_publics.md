# Public, free "maxi-prompts" for viral AI story videos (talking fruit / animals / objects, micro-dramas)

Research date: 2026-10-15. Method: web search plus direct download of the pages (raw HTML converted to text, so the prompts below are copied verbatim from the page source unless marked otherwise). Several sources are vendor blogs that sell a generator, so their claims about views and "what works" are marketing and are labeled as such.

Access limits that shape these notes:
- **Reddit could not be read.** The web search tool returned no reddit.com results for any query, WebFetch refuses reddit.com, and old.reddit.com served a login wall.
- **X/Twitter could not be read directly.** X prompts appear here only through GitHub repos that copy them with author and post links.
- **The GitHub search API was blocked in this session.** Repos were found through web search and read through raw.githubusercontent.com.

---

## Q1. Where do these maxi-prompts circulate, and which are free vs. paid?

### Takeaway
The free, verbatim, copy-pasteable prompts are mostly in:
- **Vendor/tool blogs**, which publish prompts to drive sign-ups (Vmake, Dreamina/CapCut, Flashloop, Aicut, PixPretty, YouCam/Perfect Corp, SoulVid, VidAU, EmpirioLabs).
- **Official model guides** (OpenAI Sora 2 cookbook, Google Cloud Veo 3.1 guide, fal.ai Kling 3.0 guide).
- **Large GitHub "awesome" repos** that copy prompts from X posts with credit. Those repos are mostly for Seedance 2.0.

The fruit-drama creators themselves do not publish their prompts. Some sell methods or prompt packs on Etsy, on Gumroad, and through paid "make money on TikTok" series and courses.

### Cited Findings

**GitHub repositories (free)**
- **snubroot/Veo-3-Prompting-Guide.** A large Markdown guide (v4.0) with sections including "Dialogue Generation with Lip-Sync", "Battle-Tested Dialogue Techniques", "Subtitle Prevention Techniques", "Character Template Framework", a "7-Component Professional Structure" and negative-prompt lists. It contains templates rather than fruit or animal prompts. — [GitHub](https://github.com/snubroot/Veo-3-Prompting-Guide)
- **YouMind-OpenLab/awesome-seedance-2-prompts.** Reports **6,541 prompts** (featured: 6), "Last Updated 2026-10-15", under the CC BY 4.0 license. Each prompt lists the author, the X source post and a publish date, and the repo states all prompts are "collected from the community". It includes multi-scene animal shorts (otter, cat) and comedy and drama story prompts with dialogue. — [GitHub](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts)
- **ZeroLu/awesome-seedance.** Has a "Short-form Drama & Web Series" section with timecoded, dialogue-cued Chinese micro-drama prompts copied from X user @johnAGI168, plus a "Social Media & Viral Memes" section. — [GitHub](https://github.com/ZeroLu/awesome-seedance)
- **LichAmnesia/awesome-ad-video-prompts.** Described as "Curated, original high-craft prompts for AI video ads (Seedance 2.0 / Veo 3 / Kling / Runway)", with 52 prompts across 10 formats according to the search summary. It focuses on ads, not stories. — [GitHub](https://github.com/LichAmnesia/awesome-ad-video-prompts)
- **Smaller Seedance repos and topic pages**, seen in search results only and not opened: Ericgood/seedance-prompt, apimodels/awesome-seedance2.5-prompts (its README returned 404 on the `main` branch), and the GitHub topic pages `video-prompt`, `veo` and `seedance`. — [GitHub topic video-prompt](https://github.com/topics/video-prompt); [GitHub topic seedance](https://github.com/topics/seedance)
- **No GitHub repo dedicated to talking-fruit or fruit-drama prompts was found.** A keyword scan of the YouMind README (6,541 prompts) found "fruit" only in non-character contexts, such as a fruit-market chase and a fruit stand. — [GitHub](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts)

**Blogs and vendor pages with free verbatim prompts** (examples are reproduced in Q2)
- **Talking fruit and food:**
  - Vmake (5 "master prompts", 28 June 2026) — [Vmake](https://vmake.ai/blog/ai-fruit)
  - PixPretty/Tenorshare (more than 30 talking-food prompts, 31 Aug 2026) — [PixPretty](https://pixpretty.tenorshare.ai/ai-generator/viral-talking-food-video-ai-prompts.html)
  - Dreamina (5 fruit-drama prompts) — [Dreamina](https://dreamina.capcut.com/ai-video/ai-fruit-drama)
  - Flashloop (5 fruit-soap image prompts plus motion prompts) — [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)
  - Aicut (character and multi-scene "cheating fruit" templates) — [Aicut](https://www.aicut.pro/how-to/cheating-fruits)
  - SoulVid — [SoulVid](https://www.soulvid.ai/blog/tutorials/how-to-make-an-ai-fruit-video/)
  - VidAU — [VidAU](https://www.vidau.ai/ai-fruit-story-generator-how-to-make-viral-fruit-videos/)
  - YouCam in French ("histoire de fruits", Bananito) — [YouCam FR 1](https://www.perfectcorp.com/fr/consumer/blog/generative-AI/histoire-fruit-triste-ia); [YouCam FR 2](https://www.perfectcorp.com/fr/consumer/blog/generative-AI/tendance-video-bananito)
  - YouCam talking objects — [YouCam](https://www.perfectcorp.com/consumer/blog/generative-AI/ai-talking-objects)
- **Talking creatures:** Bigfoot selfie vlogs for Veo 3. — [Ai For Real Life](https://ai-for-real-life.beehiiv.com/p/master-google-veo-3-prompts-the-bigfoot-video-breakdown-new-post); [Photutorial](https://photutorial.com/bigfoot-vlog-trend); [Kapwing](https://www.kapwing.com/resources/how-to-make-ai-bigfoot-videos-and-similar-styles/)
- **Official model guides with dialogue examples:**
  - OpenAI Sora 2 prompting guide — [OpenAI Cookbook](https://cookbook.openai.com/examples/sora/sora2_prompting_guide)
  - Google Cloud's Veo 3.1 guide — [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
  - fal.ai's Kling 3.0 guide — [fal.ai](https://blog.fal.ai/kling-3-0-prompting-guide)
  - Atlabs' Kling 3.0 templates — [Atlabs](https://www.atlabs.ai/blog/kling-3-prompt-examples-templates)
  - Replicate's Veo 3 guide — [Replicate](https://replicate.com/blog/using-and-prompting-veo-3)

**Paid or gated sources** (existence noted only; not accessed)
- **Etsy "Fruit Drama AI Prompt Pack"**, a 5-story pack for Veo 3/Google Flow plus CapCut, per the search snippet. The page returned 403 to the fetch. — [Etsy](https://www.etsy.com/listing/4503021290/fruit-drama-ai-prompt-pack-5-viral)
- **Gumroad crystal or glass-fruit ASMR packs.** One snippet cites 20 prompts for $3 and a $9.99 glass-fruit guide (not verified). — [Gumroad](https://thedigitalnesthub.gumroad.com/l/20ViralAICrystalFruitASMRVideoPrompts)
- **Gumroad Bigfoot Veo 3 packs.** — [Gumroad](https://bigfootveo.gumroad.com/l/famtdo)
- **NinjaChat "Fruit Love Island" prompts for Veo 3.1.** The search snippet says prompts are truncated behind "show full prompt". The page returned 404 at fetch time. — [NinjaChat](https://www.ninjachat.ai/fruit-love-island)
- **The French account Onlymoviesfr** ("L'île de la Skibidi Tentafruit") links from its bio to "une autre série de vidéos en accès payant proposant aux viewers de « gagner sa vie sur TikTok »". L'ADN calls selling a method or prompt after going viral "classique pour tous les producteurs de contenus slop". — [L'ADN](https://www.ladn.eu/media-mutants/lile-de-la-skibidi-tentafruit-le-short-drama-ia-le-plus-viral-du-tiktok-francais/)
- **Chinese course sellers.** According to 36Kr, many creators sell courses that "讲一遍 Seedance 2.0 的操作界面，给你一套「万能狗血剧情提示词模板」，再劝你开个 Seedance、即梦的年费会员". In English: they walk through the Seedance 2.0 interface, hand over a "universal melodrama prompt template", and push annual Seedance/Jimeng memberships. — [36Kr](https://www.36kr.com/p/3785208441598728)
- **"Veo3 JSON Prompt" app.** Listed as freemium and proprietary: $50 one-time and/or $33–39/month (search snippet). — [AlternativeTo](https://alternativeto.net/software/veo3-json-prompt)

### Inferences
- The best free source of long multi-shot prompts with timed dialogue is the Seedance GitHub repos, which mirror X posts. For talking fruit specifically, the free material is shorter single-shot prompts and fill-in templates on vendor blogs. No viral fruit account was found publishing its real production prompts.
- Paywalls in this niche are mostly low-cost packs (Etsy, Gumroad) and courses that resell generic templates. A creator can likely reconstruct the same structure from the free templates in Q2 and Q3.

### Gaps
- **Reddit (r/aivideo, r/VEO3, r/SoraAi, r/KlingAI_Videos, r/PromptEngineering):** no thread could be read or verified, for the access reasons above. The Tenten blog cites Reddit threads for Veo tips, but the links were not followed. — [Tenten](https://developer.tenten.co/veo-331-pro-json-prompting-step-by-step)
- **Public Discord and Telegram groups** sharing fruit prompts: none found in indexed sources.
- **X threads:** not directly accessible. Only the posts copied into the GitHub repos were seen.

---

## Q2. Verbatim example prompts (with source, target model, format, length)

### Takeaway
Seven groups of prompts were collected, all copied verbatim from free public pages. They split into three shapes:
- **Single-shot talking-fruit or food prompts:** prose of 25–60 words with the dialogue embedded.
- **Fill-in templates:** a cast, locations and a 5-scene story arc for "cheating fruit" dramas.
- **Long multi-shot prompts:** timecoded or labeled shots with attributed dialogue lines, the true "maxi-prompts". These come from model guides and the Seedance repos, not from fruit accounts.

### Cited Findings

#### A. Talking fruit / food / objects (single-shot, dialogue embedded)

**A1. Vmake "master prompts"** (prose, about 30–45 words each)
- **Model:** none named for the prompts. Vmake says it offers Veo 3.1, Seedance 2.0 and Kling 3.0.
- **Why they work, per Vmake:** "The secret to a phenomenal AI-generated fruit with a face lies in embedding dialogue directly into the prompt." For lip-sync, "third-party lip-syncing software can be layered over the generated footage."
- **Source:** [Vmake, 28 June 2026](https://vmake.ai/blog/ai-fruit)

> "A hyper-realistic apple with a human face looking shocked and yelling 'So you're telling me that peach fuzz on your collar is just from the farmers market? We are done!', arguing with a sly-looking mango in a modern kitchen, cinematic lighting, 4k."

> "A plump lemon with an angry face yelling, 'Who squeezed all the juice out of the household budget?! I am practically a rind over here!', Pixar style, bright studio lighting, photorealistic textures."

> "A sassy strawberry with a highly expressive human face, facing the camera and actively lip-syncing 'I am a premium berry! I refuse to be blended into a smoothie with that cheap discount spinach!', vibrant Pixar style, bright kitchen background."

> "A tough-looking avocado with a scarred face under a single bright spotlight saying 'I didn't mash him, officer. By the time I got to the cutting board, he was already guacamole', dark room, cinematic film grain, intense expression."

**A2. PixPretty / Tenorshare talking food** (more than 30 prompts, about 30–50 words each, "Says:" line appended)
- **Tools:** the page says to copy them into Leonardo.ai, Kling AI or ImagineArt. Its recommended workflow is a ChatGPT GPT → Gemini (Nano Banana) image → Flow "Frames to Video".
- **Tips from the page:**
  - "Create a 5-second clip of [food] with cartoon eyes and mouth"
  - "lip sync to this voiceover: [paste script]. Keep under 30 words for Shorts"
  - "photorealistic texture, studio lighting, 9:16 vertical, smooth 30fps"
- **Source:** [PixPretty, 31 Aug 2026](https://pixpretty.tenorshare.ai/ai-generator/viral-talking-food-video-ai-prompts.html)

> "Golden pizza slice with smug half-closed eyes and smirking mouth glaring right, cheese stretch visible, white background, 9:16. Says: "Kale? You taste like lawn clippings I make parties happen!""

> "Curly kale leaf with angry furrowed eyes and shouting mouth vs blurred donut background, dramatic lighting, 9:16 vertical. Says: "Sugar crash hits in 30 minutes. I give steady energy all day, quitter!""

> "Lemon half with wise squinted eyes and instructive mouth, pulp visible, cutting board setting, 9:16. Says: "Roll me before cutting for 2x juice. Never squeeze cut-side down or spray your eyes!""

**A3. YouCam talking objects** (structured key:value sheet plus a 10-second script)
- **Structure:** Eyes / Eyebrows / Mouth / Arms / Scene / 10-Second Script. Sold as a fit for the ChatGPT "Object Talk" style.
- **Source:** [YouCam / Perfect Corp](https://www.perfectcorp.com/consumer/blog/generative-AI/ai-talking-objects)

> "Pixar-style 3D render of a slice of cake sitting proudly on a dessert plate.
> Eyes: big, sparkling, slightly smug
> Eyebrows: lifted with confidence and charm
> Mouth: wide, frosting-lined grin
> Arms: one hand on hip, the other gesturing like a performer
> Scene: cozy kitchen table with candles glowing, warm cinematic Pixar lighting, soft crumbs and frosting texture detail
> 10-Second Script
> I'm not just dessert — I'm the moment.
> Birthdays, breakups, celebrations, regret.
> Cut me wrong, and I'll remember."

> "Pixar-style 3D render of a melting ice cream cone on a sunny sidewalk.
> Eyes: big, glossy, slightly droopy with panic
> Eyebrows: raised high, curved in alarm
> Mouth: half-melted frown, dripping mid-sentence
> Arms: one arm flailing upward, the other trying to hold itself together
> Scene: bright summer afternoon, sun glaring, soft Pixar-style depth of field, dramatic highlights on melting scoops.
> 10-Second Script: I was perfect five minutes ago. Now look at me — gravity is winning. Eat me on time or watch dreams drip away."

**A4. Dreamina fruit-drama prompts** (prose, 40–70 words, emotional close-ups, no dialogue)
- **Model:** "Dreamina Seedance 2.0", vertical 9:16.
- **Source:** [Dreamina](https://dreamina.capcut.com/ai-video/ai-fruit-drama)

> "A 3D animated, anthropomorphic strawberry character with realistic textures, standing in the pouring rain. The strawberry has large, expressive cartoon eyes filled with tears, looking deeply heartbroken and betrayed. Pixar-style, cinematic lighting, dramatic mood, highly detailed water droplets on its skin, 4k resolution, emotional close-up shot."

> "Two 3D animated fruit characters, a lemon and a lime, having a heated argument in a stylized modern kitchen. The lemon is pointing a tiny hand angrily, looking furious with furrowed brows. The lime looks defensive and surprised. Cinematic drama style, sharp focus, vibrant volumetric lighting, high-quality cartoon animation."

**A5. French-language fruit-story prompts** (YouCam FR)
- **Model:** the Bananito article says YouCam's text-to-video is "alimenté par Google Veo".
- **Sources:** [YouCam FR Bananito](https://www.perfectcorp.com/fr/consumer/blog/generative-AI/tendance-video-bananito); [YouCam FR histoire triste](https://www.perfectcorp.com/fr/consumer/blog/generative-AI/histoire-fruit-triste-ia)

> "Style cartoon 3D, Bananito la banane jaune anthropomorphe avec des yeux expressifs et des bras, assis à table avec Bananita sa femme banane, ils mangent ensemble dans une cuisine colorée, lumière chaleureuse, rendu Pixar"

> « Une poire et une pomme se tenant la main dans une cuisine, se regardant tristement avant d'être séparées, éclairage cinématographique, résolution 8K. »

#### B. Fruit soap-opera templates (multi-scene, cast sheet)

**B1. Flashloop fruit-drama image prompts** (prose, about 60–75 words; image step, then image-to-video)
- **Workflow:** Flashloop recommends 3–5 s motion prompts such as "Slow push-in on the character's face as tears form in their eyes". In motion prompts, describe characters by appearance, because "The AI doesn't know character names, only visual descriptions." Keep voiceover to "80-90 characters per scene" using ElevenLabs or PlayHT.
- **Episode shape:** 4–6 scenes: recap → rising tension → dramatic peak → cliffhanger.
- **Source:** [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)

> "Dramatic scene in a luxurious penthouse living room at night. An elderly broccoli woman in a silk ivory robe and pearl necklace stands pointing accusingly at a tall grape man in a tailored black suit. Both have intense angry expressions. Floor-to-ceiling windows showing city skyline. Warm lamp lighting with dramatic shadows. 3D animated style, photorealistic, cinematic composition, 9:16 vertical."

> "Emotional scene in a bright hospital room. An elderly broccoli woman in a hospital gown lies in bed, looking frail but determined. A young broccoli man holds her hand at the bedside, tears on his face. Medical equipment in the background, soft fluorescent lighting. 3D animated style, photorealistic, cinematic composition, 9:16 vertical."

**B2. Aicut "cheating fruits" multi-shot story template** (structured sections: CAST / LOCATIONS / STORY scenes)
- **Pipeline:** the page generates images with Nano Banana Pro and animates them with "Grok Imagine as a cost-efficient model". Each clip runs 3–8 s, with 4–8 scenes per story.
- **Source:** [Aicut](https://www.aicut.pro/how-to/cheating-fruits)

> "Premium cinematic 3D anthropomorphic fruit drama. Vertical 9:16. Ultra Realism style. No text, watermarks, or subtitles.
> CAST
> - [FRUIT TYPE] as [Name] - [Role, e.g. the betrayed wife]. Wears [outfit]. [Personality - e.g. warm, emotional, trusting].
> - [FRUIT TYPE] as [Name] - [Role, e.g. the cheating husband]. Wears [outfit]. [Personality - e.g. calm, distant, two-faced].
> - [FRUIT TYPE] as [Name] - [Role, e.g. the third party]. Wears [outfit]. [Personality - e.g. confident, glamorous, bold].
> LOCATIONS: [Primary location - e.g. modern apartment], [Secondary location - e.g. upscale office or restaurant].
> STORY
> Scene 1 - Opening: [The couple in a calm everyday moment. Establish location, mood, and characters.]
> Scene 2 - Suspicion: [Something feels off - a late message, a distant look, a suspicious call.]
> Scene 3 - Discovery: [The betrayed partner finds the truth. Close-up on their face and the reveal.]
> Scene 4 - Confrontation: [Face-to-face moment. Anger, tears, or cold silence. Maximum drama.]
> Scene 5 - Payoff: [Final emotional beat - walking out, breaking down, or a twist that changes everything.]
> Consistent wardrobe and proportions for every character across all scenes. Cinematic lighting, shallow depth of field, film grain, color grading."

**B3. Aicut character-sheet template** (used for reference images of each fruit)
- **Source:** [Aicut](https://www.aicut.pro/how-to/cheating-fruits)

> "Anthropomorphic [YOUR FRUIT] character, hyper-detailed cinematic 3D render, [YOUR FRUIT] head with realistic texture (subsurface scattering, gloss, natural surface detail), [DISTINCT FEATURE - leaves/stem/peel], expressive cartoon-human eyes, [FACIAL EXPRESSION].
> Stylized human body with [BODY TYPE], wearing [OUTFIT - specific clothing + material] with realistic fabric folds and texture.
> [POSE / ACTION], [SHOT TYPE], [CAMERA ANGLE], shallow depth of field, soft bokeh.
> Cinematic lighting: warm key light ([SOURCE]), cool fill light, rim/back light, soft shadows, realistic reflections.
> Environment: [SCENE] with [PROPS / DETAILS], softly blurred background.
> High-end 3D rendering, polished materials, ambient occlusion, film grain, cinematic color grading.
> Mood: [MOOD], color palette: [FRUIT COLORS] + [CONTRAST COLORS]."

**B4. SoulVid / VidAU short episode prompts**
- **Sources:** [SoulVid](https://www.soulvid.ai/blog/tutorials/how-to-make-an-ai-fruit-video/); [VidAU](https://www.vidau.ai/ai-fruit-story-generator-how-to-make-viral-fruit-videos/)

> "Create a vertical AI fruit drama where a blueberry chef discovers that a golden mango influencer stole her dessert recipe before a fruit market contest. Build four scenes: public reveal, confrontation, hidden proof, and cliffhanger. Keep the blueberry nervous but brave, and make the mango charming but guilty." (SoulVid)

> "Create a 9:16 comedic short featuring a confident anthropomorphic banana wearing a tiny blue jacket. He walks into a fruit café expecting applause, but nobody recognizes him. Use exaggerated facial expressions, fast camera cuts, playful dialogue and a surprise punchline in the final two seconds." (VidAU)

#### C. Talking animals / creatures

**C1. Bigfoot selfie vlog, Veo 3** (prose plus labeled Lighting / Camera / Audio blocks, about 140 words)
- **Why it works, per the author:** "Precise POV ("selfie-style," "arm's length")" and "Rich ambience".
- **Template given:** "[Camera/POV] of [character] in [location], [action/emotion], speaking to camera: "[dialogue]" Lighting: [detailed lighting] Camera: [movement, framing] Audio: [environment sounds + voice quality]"
- **Source:** [Ai For Real Life (beehiiv)](https://ai-for-real-life.beehiiv.com/p/master-google-veo-3-prompts-the-bigfoot-video-breakdown-new-post)

> "Selfie video of Bigfoot holding a handheld camera at arm's length, crouched in a misty forest near a quiet riverside campsite at golden hour. His massive, hairy face is partially lit by warm sunlight filtering through the trees. Bigfoot glances toward a group of unaware campers near a fire, then turns back to the camera with a mischievous glint in his eye and says:
> "I love this game. But if they see me… well, let's just say they won't be going home to talk about it."
> Lighting: Golden-hour sunlight with warm tones and soft shadows. Ambient mist catches light for a dreamy but eerie atmosphere.
> Camera: POV selfie-style with natural handheld sway, subtle breathing motion, slight tilt as attention shifts.
> Audio: Forest ambiance — distant camper laughter, flowing river, crackling fire. Voice is low, gravelly. No background music. No subtitles."

**C2. Shorter Bigfoot vlog prompt.** The author says it took about 5 minutes in total.
- **Source:** [Photutorial](https://photutorial.com/bigfoot-vlog-trend)

> "POV handheld camera footage of Bigfoot in dense forest, walking along a creek and picking berries, speaking directly to camera saying 'Found my favorite spot for breakfast', morning sunlight filtering through trees, birds chirping, water flowing sounds, natural movement"

**C3. Multi-scene 3D animal short, Seedance 2.0** (11 numbered scenes plus a style block; no dialogue)
- **Origin:** posted on X by "Zarnab Ai" on 3 Oct 2026. The repo's copy is cut off mid-sentence at the end ("realistic grass an").
- **Opening excerpt:**

> "Create a high-quality cinematic 3D animated short film featuring adorable, stylized baby otter-like woodland creatures in a beautiful sunny meadow.
> Scene 1: A cute brown baby otter stands in a lush green meadow, happily holding a large shiny blue berry with both paws. It has soft brown fur, a round chubby body, huge glossy black eyes, rosy cheeks, and a tiny dark scarf around its neck. The character looks innocent and curious. Warm morning sunlight, soft grass, rolling green hills, tall trees, blue sky, cinematic depth of field.
> Scene 2: The blue berry slips from the otter's paws and rolls quickly down a gentle grassy slope. [...]
> Scene 6: The gray otter and brown otter interact playfully near the hollow tree. [...] Keep their character designs consistent throughout the entire video. [...]
> Visual style: premium cinematic 3D animation, adorable family-friendly characters, soft detailed fur, expressive oversized eyes, rounded proportions, vibrant natural environment, warm golden sunlight, volumetric lighting, soft shadows [...]"

- **Source:** [YouMind awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts); original post [x.com/Zarnab_with_Ai](https://x.com/Zarnab_with_Ai/status/2106198477533544868)

**C4. "Giant Orange Cat Meme Style", Seedance 2.0** (sections in 【】 brackets plus timecoded shots, 15 s)
- **Origin:** X user @johnAGI168.
- **Source:** [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance); [X post](https://x.com/johnAGI168/status/2020717903134204344)

> "【Style】Mockumentary, mobile Vlog perspective, hyperrealistic CG combined with real scenes, 8K quality, perfect fur physics simulation.
> 【Duration】15 seconds
> 【Scene】Hongya Cave in Chongqing or a busy overpass intersection (with magical 8D city feel).
> [00:00-00:05] Shot 1: Visual spectacle (The Reveal).
> The scene shows a bustling city street. The camera lifts up to reveal a **Gozilla-sized orange tabby cat** stuck between two skyscrapers.
> Action: The giant cat is stuck because it's too fat, waving its huge paws with a pitiful expression, trying to pull itself out.
> Detail: Cat fur is clearly visible in the sunlight, huge paw pads pressing against glass curtain walls, deforming the glass.
> [00:05-00:10] Shot 2: Absurd interaction (The Interaction).
> The camera switches to ground-level perspective. Traffic flows on the street, traffic lights flashing. The giant cat lowers its head, bringing its huge cat face close to the ground, curiously sniffing a bus waiting at a red light.
> Action: The bus driver calmly reaches out and pets the giant cat's nose. The cat sneezes, instantly blowing away roadside leaves and pedestrians' hats (wind effect).
> [00:10-00:15] Shot 3: Memetic ending (The Punchline).
> The giant cat finally squeezes past the buildings and sits down on a cross-river bridge, causing the bridge deck to sink slightly (physical feedback).
> Narrative sense: It lazily lies down and starts grooming itself, blocking the entire evening rush hour traffic. The camera finally freezes on its innocent big eyes."

#### D. Multi-shot story prompts with attributed dialogue (true "maxi-prompts")

**D1. OpenAI Sora 2 official "Descriptive Prompt Template" and example** (prose, then Cinematography / Actions / Background Sound sections)
- **Template:**

> "[Prose scene description in plain language. Describe characters, costumes, scenery, weather and other details. Be as descriptive to generate a video that matches your vision.]
> Cinematography:
> Camera shot: [framing and angle, e.g. wide establishing shot, eye level]
> Mood: [overall tone, e.g. cinematic and tense, playful and suspenseful, luxurious anticipation]
> Actions:
> - [Action 1: a clear, specific beat or gesture]
> - [Action 2: another distinct beat within the clip]
> - [Action 3: another action or dialogue line]
> Dialogue:
> [If the shot has dialogue, add short natural lines here or as part of the actions list. Keep them brief so they match the clip length.]"

- **Example 1**, a talking non-human character, verbatim:

> "Style: Hand-painted 2D/3D hybrid animation with soft brush textures, warm tungsten lighting, and a tactile, stop-motion feel. The aesthetic evokes mid-2000s storybook animation — cozy, imperfect, full of mechanical charm. Subtle watercolor wash and painterly textures; warm–cool balance in grade; filmic motion blur for animated realism.
> Inside a cluttered workshop, shelves overflow with gears, bolts, and yellowing blueprints. At the center, a small round robot sits on a wooden bench, its dented body patched with mismatched plates and old paint layers. Its large glowing eyes flicker pale blue as it fiddles nervously with a humming light bulb. The air hums with quiet mechanical whirs, rain patters on the window, and the clock ticks steadily in the background.
> Cinematography:
> Camera: medium close-up, slow push-in with gentle parallax from hanging tools
> Lens: 35 mm virtual lens; shallow depth of field to soften background clutter
> Lighting: warm key from overhead practical; cool spill from window for contrast
> Mood: gentle, whimsical, a touch of suspense
> Actions:
> - The robot taps the bulb; sparks crackle.
> - It flinches, dropping the bulb, eyes widening.
> - The bulb tumbles in slow motion; it catches it just in time.
> - A puff of steam escapes its chest — relief and pride.
> - Robot says quietly: "Almost lost it… but I got it!"
> Background Sound:
> Rain, ticking clock, soft mechanical hum, faint bulb sizzle."

- **Dialogue-block example**, verbatim:

> "A cramped, windowless room with walls the color of old ash. A single bare bulb dangles from the ceiling, its light pooling onto the scarred metal table at the center. Two chairs face each other across it. On one side sits the Detective, trench coat draped across the back of his chair, eyes sharp and unblinking. Across from him, the Suspect slouches, cigarette smoke curling lazily toward the ceiling. The silence presses in, broken only by the faint hum of the overhead light.
> Dialogue:
> - Detective: "You're lying. I can hear it in your silence."
> - Suspect: "Or maybe I'm just tired of talking."
> - Detective: "Either way, you'll talk before the night's over.""

- **Rules from the guide:**
  - "Place it in a block below your prose description"
  - "label speakers consistently and use alternating turns"
  - "a 4-second shot will usually accommodate one or two short exchanges, while an 8-second clip can support a few more"
  - Extensions: "up to 20 seconds" each, "up to 6 times, for a total of 120s"
- **Source:** [OpenAI Cookbook – Sora 2 prompting guide](https://cookbook.openai.com/examples/sora/sora2_prompting_guide)

**D2. Google Veo 3.1 official timecoded multi-shot prompt and "ingredients" dialogue workflow**
- **Timestamp example:**

> "[00:00-00:02] Medium shot from behind a young female explorer with a leather satchel and messy brown hair in a ponytail, as she pushes aside a large jungle vine to reveal a hidden path.
> [00:02-00:04] Reverse shot of the explorer's freckled face, her expression filled with awe as she gazes upon ancient, moss-covered ruins in the background. SFX: The rustle of dense leaves, distant exotic bird calls.
> [00:04-00:06] Tracking shot following the explorer as she steps into the clearing and runs her hand over the intricate carvings on a crumbling stone wall. Emotion: Wonder and reverence.
> [00:06-00:08] Wide, high-angle crane shot, revealing the lone explorer standing small in the center of the vast, forgotten temple complex, half-swallowed by the jungle. SFX: A swelling, gentle orchestral score begins to play."

- **Dialogue scene with reference images**, two consecutive prompts:

> "Using the provided images for the detective, the woman, and the office setting, create a medium shot of the detective behind his desk. He looks up at the woman and says in a weary voice, "Of all the offices in this town, you had to walk into mine.""

> "Using the provided images for the detective, the woman, and the office setting, create a shot focusing on the woman. A slight, mysterious smile plays on her lips as she replies, "You were highly recommended.""

- **Source:** [Google Cloud – Ultimate prompting guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)

**D3. Kling 3.0 multi-character dialogue syntax** (bracketed speaker tags with voice and tone)
- **Example from fal.ai:**

> "A dim kitchen late at night.
> Only the refrigerator hum fills the silence.
> A plate is set down too hard.
> Ceramic clinks sharply.
> [Character A: Exhausted Partner, trembling frustrated voice]: "You never listen to me."
> Immediately, the other partner turns around, eyes wide.
> [Character B: Defensive Partner, shouting loudly]: "Because you never stop blaming!"
> The exhausted partner exhales shakily.
> [Exhausted Partner, voice cracking]: "I'm not blaming… I'm begging."
> Silence.
> [Defensive Partner, softly, regretful]: "I don't know how to fix this.""

- **fal.ai rules:**
  - "Bind dialogue to a character's unique actions. Describe the action first, then the dialogue."
  - Native multi-shot of "up to six shots"
  - Output "up to 15 seconds"
- **Source:** [fal.ai – Kling 3.0 prompting guide](https://blog.fal.ai/kling-3-0-prompting-guide)
- **Atlabs Kling 3.0 example** (using @-tagged characters):

> "Shot 1 (6s): Handheld medium shot on a snow-covered mountain ridge, wind whipping snow. @Male_hiker in red jacket laughs breathlessly: "This might be the worst idea we've ever had!" Shot 2 (9s): Camera pans to @Female_hiker in navy parka, grinning: "You said that about the last three trips too!" Natural camera shake from wind, heavy breathing, wind howling, snow crunching, cinematic winter lighting, smooth transition between characters."

- **Source:** [Atlabs](https://www.atlabs.ai/blog/kling-3-prompt-examples-templates)

**D4. Chinese micro-drama, Seedance 2.0** (【Style】【Duration】【Characters】 plus timecoded shots plus 【Dialogue lip-sync guidance】, 15 s, vertical)
- **Origin:** X user @johnAGI168.
- **Source:** [ZeroLu/awesome-seedance §6.2](https://github.com/ZeroLu/awesome-seedance); [X post](https://x.com/johnAGI168/status/2020687040853975223)

> "【Style】Popular Chinese web drama style (Mini-Drama Style), extreme fast-cut rhythm, high attractiveness filter, emotional outburst, romantic and heart-wrenching rainy night.
> 【Duration】15 seconds
> 【Characters】Deeply affectionate tycoon male lead (black coat, wet hair, red-rimmed eyes) VS stubbornly broken-hearted female lead (white dress, face full of tears).
> [00:00-00:05] Shot 1: Rapid cut combination (Rapid Cuts).
> Rainy street. Female lead decisively turns to leave (back view). Male lead rushes up and grabs her wrist (close-up). Female lead suddenly turns back, eyes showing pain filled with love and hate.
> 【Dialogue lip-sync guidance】Female lead cries out: "Let go! We're done!"
> [00:05-00:10] Shot 2: Truth explosion (Intense Close-ups).
> Male lead refuses to let go, rainwater streaming down both their faces. Male lead urgently pulls out a ring (or a document) from his chest, raises it in front of her, fingers trembling.
> 【Dialogue lip-sync guidance】Male lead shouts: "Look carefully! I never deceived you!"
> [00:10-00:15] Shot 3: Emotional dam burst (Climax).
> At the moment the female lead sees the object in her hand, her pupils shake (extreme close-up), covers her mouth, defenses collapse. The next second, the male lead suddenly pulls her into his arms and holds her tightly, as if trying to merge her into his bones. The camera quickly rotates and circles around the two embracing.
> 【Dialogue lip-sync guidance】Female lead sobs with her head down (silent/whimpering)."

- **A second example** from the same author in the same section: "Chinese Viral CEO Drama Style (Vertical Format)", a humiliation → reversal → reveal arc with three lip-synced lines. — [ZeroLu/awesome-seedance §6.3](https://github.com/ZeroLu/awesome-seedance)

**D5. "Seedance Comedy Story Video Prompt"**, the longest one found (about 6,000 characters)
- **Origin:** posted on X by 探路AI (@TanLuAI), 5 Oct 2026.
- **Section headers:** [Characters and Continuity], [0–7s: Daily Couple Dialogue], [7–9s: Hard Cut…], [9–12s…], [12–15s…], [Cinematography, Performance, and Realistic Atmosphere], [Sound], [Core Constraints].
- **Opening and a few key lines, verbatim:**

> "15 seconds, 16:9 aspect ratio, realistic live-action texture, modern Chinese urban background. The first half features natural intimate dialogue between a couple; the second half hard cuts to a Western-style wedding in a future hotel. The camera slowly pulls back to gradually reveal male guests with different colored hair, forming an absurd and awkward comedy twist. [...]
> The girl speaks completely and clearly:
> "Baby, if you're not the one marrying me in the future, you must dye your hair green to come to my wedding, so I can spot you at a glance."
> Spoken at a natural, slightly fast, coherent daily pace, not deliberately dragged out, no swallowed words, no mechanical acceleration. [...]
> [Sound]
> Opening retains girl's dialogue and slight outdoor life sounds. After hard cut, enter natural applause, fabric rustle, chair creaks, and blurred conversation of the hotel banquet hall.
> Dialogue accurately matches girl's lip movements; male lead does not speak for her or interrupt. No clear dialogue added in wedding segment.
> No narration, background music, canned laughter, twist alert sounds, or explanatory subtitles.
> [Core Constraints]
> Total length 15 seconds. The only hard cut occurs after the girl finishes her line [...]
> Information revelation order fixed: Same boy's face -> His green hair -> Same girl and different groom entering -> Surrounding gradual appearance of different colored-hair male guests -> Male lead discovers another green-haired man, looks around in surprise. [...]
> No subtitles, date stamps, explanatory text, or watermarks."

- **Source:** [YouMind awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts); [X post](https://x.com/TanLuAI/status/2106955448352231762)

**D6. Veo 3 sitcom skit with dialogue, written to avoid subtitles** (prose, about 170 words)
- **Source:** [DG Mastery (beehiiv)](https://dgmastery.beehiiv.com/p/how-to-structure-veo-3-prompts-with-dialogue-for-viral-ai-content-b8759051fa573851)

> "A classic 1980s sitcom-style scene set in a cozy, brightly lit American diner booth with pastel colors and wood accents typical of the decade. Two friends sit at a table: a heavyset, humorous man in 1980s casual clothes and his average-built friend in an era-appropriate uniform. The heavyset man has a large plate of food. With comedic seriousness, he talks to his friend about being on a diet and needing to watch what he eats, all while looking down and taking a big bite of his food. Classic canned laughter erupts as he eats, emphasizing the sitcom moment. The camera uses a medium shot to focus on both characters' facial reactions, highlighting exaggerated acting and comedic timing. The lighting is warm, with a bright color palette characteristic of 1980s television. The soundtrack features a laugh track as the punchline is delivered. Absolutely no subtitles, captions, dialogue in text, or any on-screen text appear anywhere in the video. All dialogue is performed as spoken audio only."

**D7. JSON multi-scene blueprint for Veo 3.1** (JSON with version / output / global_style / continuity.characters / scenes[])
- **Details:** generic, not a story prompt. Its fields are useful for a series: a `continuity.characters` list with reference images, and per-scene `shot`, `action`, `lighting`, `audio`. Its notes say "No text overlays or watermarks."
- **Source:** [Tenten developer blog](https://developer.tenten.co/veo-331-pro-json-prompting-step-by-step)

### Inferences
- The viral fruit accounts' polished episodes are assembled from many short clips, each with a short prompt. Flashloop gives 3–5 s clips with voiceover; Aicut gives 3–8 s clips; Brainrot Shorts says "Raw Veo 3 maxes out at ~8 seconds per generation". So a "maxi-prompt" in practice is either:
  - an **episode-level** document (cast sheet plus 4–6 scene beats plus dialogue), split into per-clip prompts, or
  - a **15 s multi-shot** prompt for Seedance 2.0 or Kling 3.0 that carries timecodes and lip-sync dialogue.

  Sources: [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos); [Aicut](https://www.aicut.pro/how-to/cheating-fruits); [Brainrot Shorts](https://www.brainrotshorts.com/ai-fruit-video-generator)
- For a fruit soap opera, combining the Aicut cast template (B2) and character sheet (B3) with the Seedance timecode and 【Dialogue lip-sync guidance】 format (D4) and the Kling speaker tags (D3) gives the most complete public structure.

### Gaps
- No verbatim production prompt from a known viral fruit account was found. Accounts checked: @ai.cinema021 (Fruit Love Island), @trombonechef, Onlymoviesfr (Skibidi Tentafruit).
- No free, verbatim Grok Imagine, Hailuo/MiniMax, Wan or LTX prompt for talking fruit or animals was found.
- The CyberLink "Fruit Love Island" sample prompt (strawberry vs banana at a villa at sunset, slow zoom, dialogue) appeared in a search summary, but the URL served the blog index when fetched. The prompt could not be verified, so it is not reproduced.

---

## Q3. What sections do these prompts contain, and what makes them work according to posters?

### Takeaway
Across sources, the recurring blocks are:
- character or cast sheet
- appearance and outfit, with a signature item
- facial expression
- action, one beat per shot
- setting and time of day
- lighting
- camera shot, movement and lens
- style or render (Pixar/3D, photoreal)
- dialogue with speaker, tone and voice
- ambient sound, SFX and music
- duration or timecodes
- aspect ratio 9:16
- negatives ("no subtitles, no text, no watermark")

Sources disagree on one formatting rule: whether to put dialogue in quotation marks.

### Cited Findings

**Official structures**
- **Google Veo 3.1 formula:** "[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]". The audio conventions are:
  - "Dialogue: Use quotation marks for specific speech (e.g., A woman says, "We have to leave now.")"
  - "SFX: thunder cracks in the distance"
  - "Ambient noise: the quiet hum of a starship bridge"

  Google also recommends describing what to exclude positively ("a desolate landscape with no buildings or roads"). — [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- **OpenAI Sora 2 "ultra-detailed" structure:** "Format & Look / Lenses & Filtration / Grade / Palette / Lighting & Atmosphere / Location & Framing / Wardrobe / Props / Extras / Sound / Optimized Shot List / Camera Notes (Why It Reads) / Finishing". The guide notes that "Shorter prompts give the model more creative freedom" and "Longer, more detailed prompts restrict the model's creativity." — [OpenAI Cookbook](https://cookbook.openai.com/examples/sora/sora2_prompting_guide)

**Community structures**
- **snubroot "7-Component Professional Structure":**
  - Subject
  - Action
  - Scene
  - Style
  - Dialogue, in the form "(Character Name): "Exact dialogue here" (Tone: emotional descriptor/delivery style)"
  - Sounds
  - "Technical (Negative Prompt): [Elements to avoid - subtitles, captions, watermarks, text overlays, unwanted objects, poor quality, artifacts]"

  Its suggested duration is "8 seconds (optimized for maximum impact)". — [GitHub snubroot](https://github.com/snubroot/Veo-3-Prompting-Guide)
- **Magic Hour speaking-shot formula:** "[Shot and camera] + [speaker] + [action] + [exact dialogue] + [delivery] + [ambience and sound] + [visual style]". Its advice: "Use one primary speaker per shot" and "If speaker attribution, timing, or lip sync fails, generate each line as a separate shot and assemble the exchange in an editor." — [Magic Hour](https://magichour.ai/blog/how-to-prompt-for-speaking-in-veo-3)
- **AI Fruit Video "fruit drama" one-liner formula:** "[fruit character] wants [visible goal], but [conflict]. Show [emotion change], [action], and "short dialogue" in [setting]. Use [camera + light], then end on [reaction or cliffhanger]." The six-part order is: character and visible goal → conflict → emotional change → action and short dialogue → setting, camera, light → reaction or cliffhanger. — [aifruitvideo.com](https://aifruitvideo.com/tools/ai-fruit-drama)

**Dialogue length**
- Replicate: dialogue "should be something that can be said in just about 8 seconds". Too long rushes the speech; too short ("Hello, I'm John") produces gibberish. — [Replicate](https://replicate.com/blog/using-and-prompting-veo-3)
- PixPretty: keep talking-food lines "under 15 words" in Flow, or "under 30 words for Shorts". — [PixPretty](https://pixpretty.tenorshare.ai/ai-generator/viral-talking-food-video-ai-prompts.html)

**Avoiding subtitles: the sources conflict**
- Replicate, for Veo 3: "put the speech you want to hear after a colon, like: "A guy says: My name is Ben" rather than in quotes", add "(no subtitles)", and if that fails, "keep saying No subtitles. No subtitles! Multiple times." — [Replicate](https://replicate.com/blog/using-and-prompting-veo-3)
- DG Mastery agrees: "use a colon, and write exactly what you want said—no quotation marks." — [DG Mastery](https://dgmastery.beehiiv.com/p/how-to-structure-veo-3-prompts-with-dialogue-for-viral-ai-content-b8759051fa573851)
- Google's own Veo 3.1 guide and Magic Hour instead recommend quotation marks for exact speech. — [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1); [Magic Hour](https://magichour.ai/blog/how-to-prompt-for-speaking-in-veo-3)
- The snubroot guide is internally inconsistent: its "WORKS" and "FAILS" subtitle examples both use `says: "..."`. — [GitHub snubroot](https://github.com/snubroot/Veo-3-Prompting-Guide)

**Other audio and pronunciation tips**
- Specify background audio to prevent hallucinated laughter: "Character tells a joke. Audio: quiet office ambiance, no audience sounds". — [GitHub snubroot](https://github.com/snubroot/Veo-3-Prompting-Guide)
- Spell names phonetically to fix mispronunciation. — [Replicate](https://replicate.com/blog/using-and-prompting-veo-3)
- One Substack tester warns that em dashes in dialogue get spoken oddly (search snippet only; not opened). — [Alejandro Dinsmore Substack](https://alejandrodinsmore.substack.com/p/deep-dive-veo-3-i-spent-400-testing)

**Character consistency: also a conflict over names**
- Flashloop: write a master prompt per character, generate 5–10 reference images, keep a "character bible", and give each character a "signature item" (pearls, red lipstick, gold watch). In motion prompts, describe by appearance, not name. — [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)
- Aicut: "In your story prompt, always refer to each character by the same name and fruit type". It also selects every character present in each scene from a reference library. — [Aicut](https://www.aicut.pro/how-to/cheating-fruits)
- AI Fruit Video: "Separate reference images will carry recurring characters' visual identities, so refer to them by name." — [aifruitvideo.com](https://aifruitvideo.com/tools/ai-fruit-drama)
- The resolution: names work only when reference images or "ingredients" carry the identity. With text-only or plain image-to-video, describe by appearance.

**Kling 3.0 dialogue rules**
- Establish characters early.
- Tag each line as `[Character, voice/tone]: "line"`.
- Put the action before the line.
- Vague attributions like "[Man] says…" are flagged as too vague.

Source: [fal.ai](https://blog.fal.ai/kling-3-0-prompting-guide)

**Story beats** (Flashloop's soap structure)
1. Recap
2. Rising tension (2–3 scenes)
3. Dramatic peak ("You're not the father!")
4. Cliffhanger ("Never resolve everything")

Per Flashloop, the top themes are infidelity reveals, then pregnancy reveals, then family dynasty drama, revenge arcs, and secret identities. This is a vendor's claim. — [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)

**Dialogue may be added after generation, not by the model**
- EmpirioLabs (Seedance 2.0 Pro "Fruit Drama" template): "The model generates ambient audio but not the spoken dialogue or subtitle overlay." Voiceover comes from a TTS tool and subtitles from CapCut. — [EmpirioLabs](https://empiriolabs.ai/blog/how-to-create-viral-fruit-drama-videos)
- Flashloop likewise uses TTS narration, with ElevenLabs or PlayHT. — [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)

### Inferences
- **Two production modes coexist.** One uses native audio with dialogue in the prompt (Veo 3/3.1, Sora 2, Kling 3.0, Seedance 2.0 multi-shot). The other generates silent or ambient clips and adds TTS voiceover and captions in CapCut, which is what Flashloop and EmpirioLabs describe for fruit dramas. A prompt template should state which mode it targets.
- **Recommended convention:** "speaker label + tone, then colon, then line", with the line in quotes only where the model's own guide asks for it (Veo 3.1, Kling 3.0), plus an explicit "No subtitles, no on-screen text" line. This seems the safest compromise between the conflicting sources.

### Gaps
- No controlled tests were found comparing quotes against no-quotes for subtitle leakage on Veo 3.1. The evidence is anecdotal or comes from guide authors.
- None of the sources measured whether longer prompts actually improved the viral fruit videos. The "what works" claims come from vendors.

---

## Q4. Are there free prompt-generator tools, GPTs or templates that output these maxi-prompts?

### Takeaway
Yes. The free options found are:
- two ChatGPT custom GPTs cited by tutorials ("Object Talk" and "Talking Food Reel Prompt Generator")
- free LLM meta-prompts on fruit-tool pages (AI Fruit Video)
- free script writing on Frutti
- several free web Veo prompt builders that export JSON
- an n8n workflow template

No maintained open-source GitHub generator built for fruit drama was found.

### Cited Findings
- **"Object Talk"** (ChatGPT, Explore GPTs). Entering an object (e.g., "banana") makes it generate "five text-to-image prompts along with five video scripts". FlexClip then runs Nano Banana Pro at 9:16 for the image and Kling 2.6 with audio for the talking clip. — [FlexClip](https://www.flexclip.com/learn/ai-talking-object-video.html)
- **Object Talk and the fruit trend.** L'ADN, citing New York Magazine, reports the fruit videos come from the same workflow: "la création d'un personnage sur Object Talk, un bot ChatGPT custom, et une animation sur l'une des nombreuses plateformes dédiées comme OpenArt". — [L'ADN](https://www.ladn.eu/media-mutants/lile-de-la-skibidi-tentafruit-le-short-drama-ia-le-plus-viral-du-tiktok-francais/). The Elmhurst Leader likewise attributes the trend's origin to Object Talk, quoting NY Mag that it lets "anyone to turn any object into a talking character with an expressive face and a quick 10-second educational monologue." — [Elmhurst Leader](https://elmhurstleader.com/stories/2026/04/something-juicy-has-entered-the-villa-fruit-ai-content-takes-over/)
- **"Talking Food Reel Prompt Generator"** (ChatGPT GPT). It returns one image prompt and one video prompt per food. The workflow continues in Gemini (Nano Banana) for the image, then Flow "Frames to Video". — [PixPretty](https://pixpretty.tenorshare.ai/ai-generator/viral-talking-food-video-ai-prompts.html)
- **AI Fruit Video free LLM meta-prompt**, pasted into ChatGPT or similar. Excerpt, verbatim:

  > "I'm creating a fruit story video on aifruitvideo.com. Please help me develop the story and write the prompts I'll use to generate each video clip. I want to create a love story starring stylized anthropomorphic fruit characters with clearly recognizable fruit forms and textures, along with expressive, human-like faces and bodies. [...] Please also provide a concise character guide for each recurring character: fruit identity, defining visual traits, personality, and a reusable base appearance for character reference images. [...] Once we have discussed and settled on the story, break it into video clips in story order. Give each clip a short title and a compact natural-language description ready to use as the prompt for generating one video clip. [...] Keep most clips focused on one or two visible characters and one clear action or emotional beat in a single setting and continuous moment."

  — [aifruitvideo.com](https://aifruitvideo.com/tools/ai-fruit-drama)
- **Frutti.** "Writing the whole episode is free on this page: the script, the cast and the scene list, with no account and no card." Rendering is paid: Starter is $24/month for 1,200 credits, which is one Standard 30 s episode (3×10 s clips). Prices checked 12 Sep 2026. — [Frutti](https://frutti.ai/talking-fruit-video-generator)
- **Kapwing's ChatGPT seeding prompt** for consistent character prompts (the Bigfoot case): "I'm working on a video project using Gemini Veo 3 and need help writing consistent prompts for an AI video generator. Each prompt should feature my main character, [a personified Sasquatch who wears a black baseball cap with the word "YOWIE" stitched on the front]." — [Kapwing](https://www.kapwing.com/resources/how-to-make-ai-bigfoot-videos-and-similar-styles/)
- **Free Veo prompt builders and JSON tools** (all from search snippets; not opened or tested):
  - Gradually.ai Veo 3 Prompt Generator (free; exports JSON, YAML, Markdown, XML) — [Gradually.ai](https://www.gradually.ai/veo-prompt-generator/)
  - Groww Stacks n8n workflow (free template converting plain English into Veo 3 JSON via GPT plus Gemini; needs your own API keys) — [Groww Stacks](https://www.growwstacks.com/workflows/convert-natural-language-to-video-json-prompts-with-gpt-and-gemini-for-veo-3)
  - "Veo3jsonprompts / Prompt Atlas" (free library of JSON examples) — [Toolmage](https://www.toolmage.com/en/tool/veo3jsonprompts/)
  - A "veo-3.2-prompter" agent skill that outputs one JSON object — [skills.sh](https://www.skills.sh/pexoai/pexo-skills/veo-3.2-prompter)
  - A GitHub Pages-hosted "JSON-Prompt-Gen" guide — [solvingtools.github.io](https://solvingtools.github.io/JSON-Prompt-Gen/src/blog/veo-json-prompt-guide/)
- **Gated or paid generators:**
  - The Aicut "Clone Prompt" feature: "Enter a Tiktok Video URL and let aicut analyze it to get the video scene prompts". — [Aicut](https://www.aicut.pro/how-to/cheating-fruits)
  - The "Veo3 JSON Prompt" app, which is paid — [AlternativeTo](https://alternativeto.net/software/veo3-json-prompt)

### Inferences
- The most practical free maxi-prompt generator is an LLM with a good meta-prompt, such as the AI Fruit Video template above, combined with the structures in Q3. The dedicated "JSON generators" mostly reformat the same fields.

### Gaps
- Whether the GPTs "Object Talk" and "Talking Food Reel Prompt Generator" are still live, and who publishes them, was not verified. ChatGPT GPT pages were not accessed.
- No open-source GitHub generator repo for Veo or fruit prompts was confirmed, because the GitHub search API was unavailable here.

---

## Q5. Which tools do fruit-drama creators reportedly use, and do they publish templates?

### Takeaway
Reporting and tutorials name a mixed stack:
- **Scripts and prompts:** ChatGPT, including the Object Talk GPT.
- **Character images:** Nano Banana or Nano Banana Pro, via Gemini, OpenArt or Flashloop.
- **Animation:** Kling, Veo 3/3.1 (Flow), Seedance 2.0 (Dreamina/Jimeng), and Grok Imagine as a cheap bulk option.
- **Voice and edit:** ElevenLabs or another TTS, then CapCut.

TrendStory.io and FruitDrama.io were not found in any indexed source. The original viral accounts have not published their prompt templates.

### Cited Findings
- **Fruit Love Island facts:**
  - Launched 13 March 2026 by @ai.cinema021.
  - More than 3 million followers in nine days and more than 300 million total views, averaging over 10 million per episode.
  - Production halted on 28 March 2026.
  - It "combines various types of generative AI, including those for visuals, voice-overs, and script generation".

  The creator's identity is unconfirmed. — [Wikipedia](https://en.wikipedia.org/wiki/Fruit_Love_Island)
- **Production details:**
  - Per @ai.cinema021, one episode takes "about 3 hours to produce"; episodes run about 2–4 minutes. — [GIGAZINE](https://wbgsv0a.gigazine.net/gsc_news/en/20260330-fruit-love-island-ai-movie)
  - The creator posted an online document for viewers to submit plot ideas. — [36Kr](https://www.36kr.com/p/3785208441598728)
  - Wikipedia says audience votes "usually took place in a Google Form". — [Wikipedia](https://en.wikipedia.org/wiki/Fruit_Love_Island)
- **Origin of the cheating-fruit trend:** a late-February 2026 TikTok of a strawberry cheating with an eggplant. Creator @trombonechef first called it a "sad fruit story" and the video reached more than 26 million views. — [Daily Dot](https://lede-v2.dailydot.com/ai-slop-videos-of-cheating-fruit-are-taking-over-tiktok)
- **French scene:** Onlymoviesfr's "L'île de la Skibidi Tentafruit" runs about 5-minute episodes with up to 9 million views per episode, adapted from AI Cinema's format. The bio links to a paid "gagner sa vie sur TikTok" series. — [L'ADN](https://www.ladn.eu/media-mutants/lile-de-la-skibidi-tentafruit-le-short-drama-ia-le-plus-viral-du-tiktok-francais/). Presse-citron also lists "Pascal le Grand Fruit" and notes brands (Oasis, Danette, Free, Picard) engaging in the comments. — [Presse-citron](https://www.presse-citron.net/cest-nul-mais-tout-le-monde-regarde-les-fruits-ia-explosent-les-compteurs-sur-tiktok/)
- **Tool stacks reported in tutorials:**
  - Aicut: Nano Banana Pro images, then Grok Imagine video ("the most cost-efficient choice for bulk scene generation"), with key scenes optionally re-rendered on a better model. — [Aicut](https://www.aicut.pro/how-to/cheating-fruits)
  - Flashloop claims "Several of the biggest fruit drama accounts use Flashloop for their image generation" and that its watermark appears on viral clips. This is an unverified vendor claim. — [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)
  - Dreamina pushes Seedance 2.0 with "First and last frame" and Multiframes for Fruit Love Island-style clips. — [Dreamina FLI](https://dreamina.capcut.com/ai-video/ai-fruit-love-island)
- **Costs:**
  - Brainrot Shorts estimates the DIY stack at "Veo 3 ($20) + Kling ($10) + ElevenLabs ($22) + CapCut Pro ($8) = ~$60/mo". — [Brainrot Shorts](https://www.brainrotshorts.com/ai-fruit-video-generator)
  - 36Kr (China): Seedance 2.0 API costs about 46 yuan per million tokens, and a 15 s video uses about 308,880 tokens, or roughly 15 yuan per attempt. With 3–5 attempts per usable clip and several 15 s clips per 1-minute video, a publishable video costs "数百元" (several hundred yuan). — [36Kr](https://www.36kr.com/p/3785208441598728)
- **Talking-object variants:** after fruit, Chinese creators moved to anthropomorphized phones, AirPods, bottled water, milk tea and jewelry in 30 s divorce, cheating and pregnancy plots. — [36Kr](https://www.36kr.com/p/3785208441598728)
- **Industry signal:** SocialPeta's ranking for 13–19 July 2026 named "fruit-personification melodrama" among the week's three standout micro-drama themes, out of about 43,200 active titles (search snippet). — [SocialPeta](https://socialpeta.com/en/blog/short-drama-weekly-ranking-43k-titles-compete-as-ai-dramas-rise-and-fruit-themed-melodramas-expand-globally)
- **Originality dispute:** creator Joy Ofodu said the Fruit Love Island concept drew on her earlier fruit-personality videos (search snippet). — [AOL](https://www.aol.com/articles/black-creator-says-ai-fruit-164743347.html)

### Inferences
- The original creators keep their prompts private and monetize attention through follows, YouTube, and sometimes paid methods. Every public "template" comes from tool vendors reverse-engineering the format. Vendor templates largely agree on the structure: cast sheet, then reference images, then 3–8 s clips per beat, then TTS and captions.

### Gaps
- **TrendStory.io and FruitDrama.io:** several searches returned nothing under these names, so they cannot be confirmed as tools fruit creators use.
- **Which model @ai.cinema021 actually used** is not confirmed by any primary source. Press coverage says only "multiple AIs".
- **A tutorial pipeline** (ChatGPT prompts → OpenArt with Nano Banana Pro → Kling) appeared in a search summary of an alici.ai page, but the page returned 403. It is unverified.
- **The New York Magazine article** about Object Talk was not fetched directly; it is cited only through L'ADN and the Elmhurst Leader.
