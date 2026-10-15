# Démonter les maxi-prompts pour bâtir « Rue des Fruits »

**Il n'existe pas de maxi-prompt secret à recopier** : aucun des comptes de fruits qui ont fait des centaines de millions de vues (Fruit Love Island, @trombonechef, L'Île de la Skibidi Tentafruit) n'a publié ses prompts. Ce qui circule gratuitement vient des blogs de vendeurs d'outils, des guides officiels des modèles et de quelques dépôts GitHub qui recopient des prompts publiés sur X, surtout pour Seedance 2.0 (6 541 prompts sous licence CC BY 4.0 dans le plus gros). Toutes ces sources décrivent la même anatomie : un style nommé d'emblée, un bloc personnage figé copié mot pour mot à chaque plan, un décor et sa lumière, un seul mouvement de caméra, l'action découpée en battements, la réplique exacte entre guillemets rattachée à un geste, à un ton et à une langue, une consigne sonore séparée, puis les interdits (pas de sous-titres, pas de second locuteur). Le « maxi » n'est pas dans chaque prompt mais dans le document d'épisode (bible, distribution, battements, dialogues), que l'on découpe ensuite en clips de 3 à 8 secondes ; seuls les modèles payants récents (Seedance, Kling, Grok) acceptent un prompt unique de 15 secondes à plusieurs plans minutés. La constance des personnages ne s'obtient pas par le texte seul : il faut des fiches figées, des images de référence, un accessoire signature par personnage et, pour la voix, un traitement après coup, ce que nos voix clonées font déjà mieux que n'importe quel modèle à audio natif. Côté histoire, les séries qui ont marché ouvrent sur une réplique choc dès la première seconde, escaladent, retournent la situation et coupent net sur « Partie 2 ». La tromperie suivie d'une révélation de paternité est le trope le plus éprouvé, et la deuxième partie de @trombonechef a fait 24 millions de vues contre 2,9 millions pour la première. Pour notre chaîne gratuite, la consigne est nette : LTX veut un seul paragraphe au présent de 4 à 8 phrases, le style nommé tôt, la réplique française entre guillemets coupée en segments avec une indication de jeu, le son à la fin et les interdits dans le champ négatif. Le JSON ne sert qu'à notre organisation interne, et la plupart des astuces des modèles payants (voix liées, références multiples, multi-plans minutés) ne nous concernent pas. Aucune source fiable ne documente un nouveau format apparu en septembre ou octobre 2026 : la dernière vague décrite date du printemps, même si notre propre échantillon de vidéos françaises montre que le genre fait encore 1 à 4 millions de vues par épisode. Le rapport se termine par deux gabarits prêts à remplir, l'un pour le prompt d'un plan, l'autre pour faire écrire la liste de plans par un modèle de langage.

## Les prompts des comptes viraux restent privés, les gabarits gratuits sont ailleurs

### Petit lexique

| Terme | Sens dans ce rapport |
|---|---|
| Maxi-prompt | Consigne longue et structurée donnée à un modèle vidéo : personnages, décor, caméra, jeu, réplique mot pour mot, son, interdits. |
| Plan | Un clip généré d'un seul tenant (3 à 8 s chez nous), entre deux coupes du montage. |
| Image clé | L'image fixe fabriquée d'abord, que le modèle vidéo anime ensuite. |
| T2V, I2V, R2V | Texte → vidéo ; image → vidéo (l'image devient la première image) ; référence → vidéo (des images montrent les personnages sans imposer la première image). |
| Bloc fixe, bloc variable | Le bloc fixe (style, personnage, décor, voix) est recopié à l'identique d'un plan à l'autre ; seul le bloc variable (action, caméra, réplique) change. |
| Timecode | Repère de temps dans un prompt multi-plans, par exemple `[00:00-00:05]`. |
| Champ négatif | Case séparée où l'on liste ce que le modèle doit éviter (sous-titres, second personnage…). |
| Lip-sync | Synchronisation des lèvres avec la voix. |
| LoRA | Petit module entraîné pour qu'un modèle redessine fidèlement un personnage précis. |
| Bible | Le document de référence de la série : personnages, tenues, décors, voix, règles. |
| Cliffhanger | Fin coupée en plein suspense, qui pousse à regarder la suite. |

### Ceux qui font les vues ne montrent pas leurs prompts

Les créateurs à l'origine de la mode n'ont jamais publié leurs consignes. *Fruit Love Island*, lancée le 13 mars 2026 par le compte anonyme @ai.cinema021, a dépassé 3 millions d'abonnés en neuf jours et 300 millions de vues ; Wikipedia en dit seulement qu'elle « combines various types of generative AI, including those for visuals, voice-overs, and script generation » ([Wikipedia](https://en.wikipedia.org/wiki/Fruit_Love_Island)). Le créateur dit mettre **environ 3 heures par épisode** de 2 à 4 minutes ([GIGAZINE](https://wbgsv0a.gigazine.net/gsc_news/en/20260330-fruit-love-island-ai-movie)). Le seul indice sur sa méthode vient de New York Magazine, repris par L'ADN : les personnages naîtraient dans « Object Talk », un GPT personnalisé de ChatGPT, puis seraient animés sur une plateforme comme OpenArt ([L'ADN](https://www.ladn.eu/media-mutants/lile-de-la-skibidi-tentafruit-le-short-drama-ia-le-plus-viral-du-tiktok-francais/)). Ce GPT permet à « anyone to turn any object into a talking character with an expressive face and a quick 10-second educational monologue » ([Elmhurst Leader](https://elmhurstleader.com/stories/2026/04/something-juicy-has-entered-the-villa-fruit-ai-content-takes-over/)). Les comptes @trombonechef et Onlymoviesfr n'ont rien publié non plus. Le second renvoie depuis sa bio vers une série payante pour « gagner sa vie sur TikTok », un geste que L'ADN juge « classique pour tous les producteurs de contenus slop » ([L'ADN](https://www.ladn.eu/media-mutants/lile-de-la-skibidi-tentafruit-le-short-drama-ia-le-plus-viral-du-tiktok-francais/)).

Le marché payant qui s'est formé autour vend surtout des gabarits génériques. On trouve un « Fruit Drama AI Prompt Pack » de cinq histoires pour Veo 3 et CapCut sur Etsy ([Etsy](https://www.etsy.com/listing/4503021290/fruit-drama-ai-prompt-pack-5-viral)), des lots de prompts ASMR de fruits en verre à quelques dollars sur Gumroad ([Gumroad](https://thedigitalnesthub.gumroad.com/l/20ViralAICrystalFruitASMRVideoPrompts)), des prompts « Fruit Love Island » tronqués derrière un bouton chez NinjaChat ([NinjaChat](https://www.ninjachat.ai/fruit-love-island)) et une application « Veo3 JSON Prompt » à 50 $ ou 33 à 39 $ par mois ([AlternativeTo](https://alternativeto.net/software/veo3-json-prompt)). En Chine, 36Kr décrit des vendeurs de cours qui présentent l'interface de Seedance 2.0, donnent un « 万能狗血剧情提示词模板 » (un « gabarit universel de prompt pour mélodrame ») et poussent à prendre un abonnement annuel ([36Kr](https://www.36kr.com/p/3785208441598728)). Rien de tout cela n'est nécessaire : **les gabarits gratuits décrits plus bas couvrent la même structure**, et les vendeurs eux-mêmes les ont reconstitués par rétro-ingénierie.

### Où trouver gratuitement des prompts complets

| Source | Ce qu'on y trouve | Modèle visé | Intérêt pour Rue des Fruits |
|---|---|---|---|
| [YouMind awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) | **6 541 prompts** sous licence CC BY 4.0, chacun avec son auteur et le lien du message X d'origine ; courts métrages d'animaux à plusieurs scènes, comédies et drames avec dialogues ; le plus long fait environ 6 000 caractères | Seedance 2.0 | Le meilleur stock de prompts longs, minutés, avec contraintes et son |
| [ZeroLu awesome-seedance](https://github.com/ZeroLu/awesome-seedance) | Une section « Short-form Drama & Web Series » : des micro-dramas chinois minutés, avec répliques à synchroniser, recopiés de @johnAGI168 | Seedance 2.0 | Le format le plus proche d'un feuilleton |
| [snubroot Veo-3-Prompting-Guide](https://github.com/snubroot/Veo-3-Prompting-Guide) et [Veo-3-Meta-Framework](https://github.com/snubroot/Veo-3-Meta-Framework) | Gabarits de personnage, de dialogue, techniques contre les sous-titres, listes de négatifs | Veo 3 / 3.1 | Gabarits de fiches et listes d'interdits |
| Guides officiels : [Google Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1), [Sora 2](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide), [Kling 3.0](https://kling.ai/quickstart/klingai-video-3-model-user-guide), [xAI](https://docs.x.ai/developers/model-capabilities/video/overview), [Alibaba Wan](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt), [LTX](https://ltx.io/blog/directing-dialogue-and-acting) | La doctrine de chaque éditeur, avec des exemples de dialogues complets | chacun le sien | **Le guide LTX est le seul qui vise notre moteur** |
| Blogs de fruits parlants : [Vmake](https://vmake.ai/blog/ai-fruit), [PixPretty](https://pixpretty.tenorshare.ai/ai-generator/viral-talking-food-video-ai-prompts.html), [Dreamina](https://dreamina.capcut.com/ai-video/ai-fruit-drama), [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos), [Aicut](https://www.aicut.pro/how-to/cheating-fruits), [SoulVid](https://www.soulvid.ai/blog/tutorials/how-to-make-an-ai-fruit-video/), [VidAU](https://www.vidau.ai/ai-fruit-story-generator-how-to-make-viral-fruit-videos/), [YouCam en français](https://www.perfectcorp.com/fr/consumer/blog/generative-AI/tendance-video-bananito) | Prompts d'un plan de 25 à 75 mots, gabarits de distribution « fruits infidèles », structure d'épisode | Veo, Seedance, Kling, Grok | Le vocabulaire visuel des fruits et les gabarits de casting |
| Méta-prompts gratuits : [aicut.pages.dev](https://aicut.pages.dev/), [aifruitvideo.com](https://aifruitvideo.com/tools/ai-fruit-drama) | Consignes à coller dans ChatGPT pour obtenir histoire, fiches et un prompt par clip | tous | La base de notre gabarit 2 |
| Pipelines libres : [drama-skills](https://github.com/zenstory-ai/drama-skills/blob/main/README_EN.md) (MIT), [ViMax](https://github.com/HKUDS/ViMax) (MIT), [Toonflow](https://github.com/HBAI-Ltd/Toonflow-app) (MIT), [huobao-drama](https://github.com/chatfire-AI/huobao-drama) (CC BY-NC-SA, non commercial) | Chaînes histoire → découpage → prompts → images → vidéo | surtout des API payantes | drama-skills écrit des fichiers Markdown avec des « verrous de continuité » : la méthode la plus proche de la nôtre |

Le prompt français de YouCam montre au passage qu'on peut écrire toute la consigne en français, même si la plupart des guides préfèrent l'anglais : « Style cartoon 3D, Bananito la banane jaune anthropomorphe avec des yeux expressifs et des bras, assis à table avec Bananita sa femme banane, ils mangent ensemble dans une cuisine colorée, lumière chaleureuse, rendu Pixar » ([YouCam](https://www.perfectcorp.com/fr/consumer/blog/generative-AI/tendance-video-bananito)). Plusieurs générateurs gratuits produisent aussi ces prompts tout seuls. « Object Talk » renvoie, pour un objet donné, « five text-to-image prompts along with five video scripts » ([FlexClip](https://www.flexclip.com/learn/ai-talking-object-video.html)). Frutti écrit gratuitement le script, la distribution et la liste de scènes, mais facture le rendu à 24 $ par mois pour un épisode de 30 secondes ([Frutti](https://frutti.ai/talking-fruit-video-generator)). Gradually.ai exporte des prompts Veo en JSON, YAML ou Markdown ([Gradually.ai](https://www.gradually.ai/veo-prompt-generator/)). Aucun dépôt GitHub consacré aux fruits parlants n'a été trouvé : une recherche de « fruit » dans les 6 541 prompts de YouMind ne trouve que des marchés et des étals ([YouMind](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts)).

**Une lacune pèse sur tout ce rapport : Reddit n'a pas pu être lu.** L'outil de recherche ne renvoyait aucun résultat reddit.com, la lecture directe était refusée et old.reddit.com affichait une page de connexion. Les fils de r/aivideo, r/VEO3 ou r/PromptEngineering ne sont donc connus qu'à travers les blogs qui les citent. X n'a été lu qu'à travers les copies des dépôts GitHub, et aucun groupe Discord ou Telegram public n'est apparu.

### Ce que le marché a changé depuis le printemps

Plusieurs repères ont bougé depuis l'été. **L'API Sora 2 a fermé le 24 septembre 2026** : « The Sora 2 models and Videos API were shut down on September 24, 2026 and are no longer available » ([OpenAI](https://developers.openai.com/api/docs/guides/video-generation.md)). Son guide de prompts reste en ligne « for historical reference » et sert encore de doctrine. Google recommande désormais Gemini Omni Flash comme modèle vidéo par défaut, et réserve Veo 3.1 à l'extension de scène et au contrôle de la dernière image ([Gemini API](https://ai.google.dev/gemini-api/docs/video)). Chez Lightricks, LTX-2.5 serait sorti le 11 août 2026 avec un mode multi-plans natif (source tierce : [ComfyUI-Wiki](https://comfyui-wiki.com/en/news/2026-08-11-ltx-2-5-open-weights-release)), et le dépôt officiel classe LTX-2.3 comme « Legacy » ([GitHub LTX-2](https://github.com/Lightricks/LTX-2)). xAI propose Grok Imagine Video 1.5, avec parole synchronisée et références vocales ([xAI](https://docs.x.ai/developers/model-capabilities/video/overview)). Pour Agnes, la seule fiche trouvée concerne Agnes-Video-V2.0 de Sapiens AI ([ZenMux](https://zenmux.ai/sapiens-ai/agnes-video-v2.0)) ; **aucune documentation n'existe pour agnes-video-2.5-flash**, et notre README note que la version 2.0 a disparu de l'API le 9 octobre.

## Un maxi-prompt empile les mêmes blocs, du style aux interdits

### Trois formes circulent, de la phrase de 30 mots au scénario de 6 000 caractères

La forme la plus courte est **le plan unique avec réplique intégrée**, 25 à 60 mots de prose. C'est celle des blogs de fruits parlants. Vmake affirme que « The secret to a phenomenal AI-generated fruit with a face lies in embedding dialogue directly into the prompt », et propose par exemple ([Vmake](https://vmake.ai/blog/ai-fruit)) :

> "A plump lemon with an angry face yelling, 'Who squeezed all the juice out of the household budget?! I am practically a rind over here!', Pixar style, bright studio lighting, photorealistic textures."

Tout y est en miniature : l'espèce, l'émotion, le verbe de parole, la réplique, le style, la lumière. Il manque la caméra, le décor et les interdits, ce qui suffit pour un plan isolé mais pas pour une série. YouCam ajoute une idée utile pour des fruits, qui n'ont pas de visage par défaut : **décrire l'anatomie du visage champ par champ** ([YouCam](https://www.perfectcorp.com/consumer/blog/generative-AI/ai-talking-objects)).

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

La deuxième forme est **le gabarit de feuilleton à remplir**, qui fixe la distribution, les lieux et l'arc d'un épisode avant tout plan. Aicut publie celui des « fruits infidèles », dont les images sont faites avec Nano Banana Pro puis animées en clips de 3 à 8 secondes, 4 à 8 scènes par histoire ([Aicut](https://www.aicut.pro/how-to/cheating-fruits)) :

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

Ce gabarit n'est pas envoyé tel quel au modèle vidéo : il sert de document d'épisode, d'où l'on tire ensuite un prompt par scène. Flashloop en donne la version image, où chaque personnage est désigné par son apparence et où une même formule de style termine chaque prompt ([Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)) : « Dramatic scene in a luxurious penthouse living room at night. An elderly broccoli woman in a silk ivory robe and pearl necklace stands pointing accusingly at a tall grape man in a tailored black suit. Both have intense angry expressions. Floor-to-ceiling windows showing city skyline. Warm lamp lighting with dramatic shadows. 3D animated style, photorealistic, cinematic composition, 9:16 vertical. »

La troisième forme est **le vrai maxi-prompt multi-plans**, minuté et dialogué, pour une génération de 15 secondes. Il vient des dépôts Seedance, pas des comptes de fruits. Voici un micro-drama chinois de @johnAGI168, en vertical ([ZeroLu awesome-seedance](https://github.com/ZeroLu/awesome-seedance) ; [message X](https://x.com/johnAGI168/status/2020687040853975223)) :

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

Les blocs entre crochets fixent le style, la durée et les personnages une fois pour toutes ; chaque plan porte ensuite son timecode, une action visible et une seule réplique, rattachée nommément à son locuteur. Le plus long prompt trouvé, une comédie de 15 secondes publiée par @TanLuAI le 5 octobre 2026 (environ 6 000 caractères), pousse la logique plus loin : il **écrit le rebondissement comme une contrainte**, en imposant l'ordre dans lequel l'information se révèle, et règle le débit de la parole et le son ([YouMind](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) ; [message X](https://x.com/TanLuAI/status/2106955448352231762)) :

> "Spoken at a natural, slightly fast, coherent daily pace, not deliberately dragged out, no swallowed words, no mechanical acceleration. [...]
> [Sound]
> Opening retains girl's dialogue and slight outdoor life sounds. After hard cut, enter natural applause, fabric rustle, chair creaks, and blurred conversation of the hotel banquet hall.
> Dialogue accurately matches girl's lip movements; male lead does not speak for her or interrupt. No clear dialogue added in wedding segment.
> No narration, background music, canned laughter, twist alert sounds, or explanatory subtitles.
> [Core Constraints]
> Total length 15 seconds. The only hard cut occurs after the girl finishes her line [...]
> Information revelation order fixed: Same boy's face -> His green hair -> Same girl and different groom entering -> Surrounding gradual appearance of different colored-hair male guests -> Male lead discovers another green-haired man, looks around in surprise. [...]
> No subtitles, date stamps, explanatory text, or watermarks."

Les éditeurs de modèles publient des exemples du même niveau, qui servent de référence de ton. Le guide de Sora 2 montre la version à blocs étiquetés, où la parole est une action parmi d'autres ([OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)) :

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

Le guide Kling 3.0 de fal, partenaire officiel de Kling, montre une dispute de couple à deux locuteurs : chaque réplique est précédée d'un geste, d'une étiquette de personnage unique et d'une consigne de voix, et un mot de liaison (« Immediately ») empêche le modèle de fondre deux répliques en une ([fal](https://blog.fal.ai/kling-3-0-prompting-guide)) :

> "A dim kitchen late at night. Only the refrigerator hum fills the silence. A plate is set down too hard. Ceramic clinks sharply. [Character A: Exhausted Partner, trembling frustrated voice]: "You never listen to me." Immediately, the other partner turns around, eyes wide. [Character B: Defensive Partner, shouting loudly]: "Because you never stop blaming!" The exhausted partner exhales shakily. [Exhausted Partner, voice cracking]: "I'm not blaming… I'm begging." Silence. The defensive partner sighs heavily. [Defensive Partner, softly, regretful]: "I don't know how to fix this." A sad piano chord enters quietly."

xAI ajoute un bloc que les autres oublient : **la continuité écrite noir sur blanc**. Son exemple officiel de dispute au café se termine par « Continuity: café, table, two cups, the plate with exactly two croissants, and the window match in both shots; nobody touches the croissants; nothing appears, disappears or changes shape. Natural lip sync for each speaker » ([xAI](https://docs.x.ai/developers/model-capabilities/video/overview)). Enfin, l'exemple qui compte le plus pour nous vient de Lightricks, car c'est notre moteur. Le guide de LTX-2.3 coupe la réplique en morceaux et glisse une seule indication de jeu entre deux morceaux ([LTX](https://ltx.io/blog/directing-dialogue-and-acting)) :

> "A man in his late fifties with greying stubble sits at a wooden kitchen table in a warm, dim room. He speaks in a slow, weary voice, "I never told you this..." He pauses and looks at his hands, then continues, "but I almost left..." His shoulders drop. He finishes, voice catching, "the year you were born." The camera holds the frame. Faint room tone, a refrigerator hum, no music."

Ces trois formes répondent à deux modes de production qui coexistent. Le premier confie la voix au modèle : la réplique est dans le prompt, comme chez Veo, Sora, Kling ou Seedance. Le second génère des plans muets ou d'ambiance, puis ajoute au montage une voix de synthèse et des sous-titres. EmpirioLabs le dit pour son gabarit Seedance de fruits : « The model generates ambient audio but not the spoken dialogue or subtitle overlay » ([EmpirioLabs](https://empiriolabs.ai/blog/how-to-create-viral-fruit-drama-videos)). Flashloop fait de même avec un narrateur unique sous ElevenLabs ou PlayHT ([Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)). **Notre chaîne est un hybride** : le modèle prononce la réplique pour animer les lèvres et le jeu, puis nos voix clonées remplacent la sienne. Le prompt doit donc rester du premier type, même si le timbre qu'il décrit ne sera jamais entendu.

### L'ordre des blocs fait consensus chez tous les éditeurs

Chaque éditeur a sa formule. Google écrit « [Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance] » et voit dans la caméra « the most powerful tool for conveying tone and emotion » ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)). Alibaba écrit « Entity + Scene + Motion + Aesthetic control + Stylization » et prévient que « Most weak prompts cover entity and motion but skip aesthetic control and stylization — producing a static camera in an undefined void » ([Alibaba Cloud](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt)). Seedance 1.5 écrit « Subject + Movement + Environment + Camera movement + Aesthetic description + Sound » ([BytePlus](https://docs.byteplus.com/en/docs/ModelArk/seedance-1-5-pro)). LTX, enfin, demande de tout écrire « in a single flowing paragraph », en commençant directement par l'action ([GitHub LTX-2](https://github.com/Lightricks/LTX-2)). Sous ces variantes, le squelette est le même, et c'est lui que reprend notre gabarit.

| Bloc | Ce qu'on y met | Formulation type tirée des sources | Source |
|---|---|---|---|
| 1. Style et format | Rendu, époque, 9:16, nommés en premier | « Establish this style early so the model can carry it through consistently » ; « Cinematic look » trop vague, préférer « Anamorphic 2.0x lens, shallow DOF, volumetric light » | [OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) ; [LTX](https://ltx.io/blog/prompting-guide-for-ltx-2) |
| 2. Personnage | Une phrase figée, copiée mot pour mot : espèce, peau, visage, cheveux, silhouette, tenue, accessoire signature | « Anchoring your subject with a few distinctive details keeps it recognizable » | [OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) |
| 3. Décor, lumière, palette | Lieu, moment, 3 à 5 repères, source de lumière, 3 à 5 couleurs | « Naming three to five colors helps keep the palette stable across shots » ; « Wet asphalt, zebra crosswalk, neon signs reflecting in puddles » | [OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) |
| 4. Caméra | Taille de plan, angle, **un seul** mouvement ou caméra fixe | « Each shot should have one clear camera move and one clear subject action » | [OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) |
| 5. Action en battements | Gestes comptés, au présent, avant la parole | « Actor takes four steps to the window, pauses, and pulls the curtain in the final second » | [OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) |
| 6. Dialogue | Locuteur unique, ton, langue, réplique exacte | « Bind dialogue to a character's unique actions. Describe the action first, then the dialogue » | [fal](https://blog.fal.ai/kling-3-0-prompting-guide) |
| 7. Son | Ambiance, un ou deux bruits liés à l'action, musique ou « no music » | « We recommend that you use separate sentences in your prompt to describe the audio » | [Google Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide) |
| 8. Continuité et interdits | Qui parle seul, ce qui ne doit ni apparaître ni disparaître, pas de texte | « nothing appears, disappears or changes shape » | [xAI](https://docs.x.ai/developers/model-capabilities/video/overview) |
| 9. Durée et découpage | Durée, timecodes ou « single continuous shot » | « If you need the output video to contain a single scene, you must prompt for that » | [Gemini API](https://ai.google.dev/gemini-api/docs/omni) |

Le format compte moins que la discipline. Le guide Veo 3 de snubroot résume ce squelette en sept composants (sujet, action, scène, style, dialogue, sons, négatif) et donne une syntaxe de dialogue reprise partout : « (Character Name): "Exact dialogue here" (Tone: emotional descriptor/delivery style) » ([GitHub snubroot](https://github.com/snubroot/Veo-3-Prompting-Guide)). Le prompt de vlog « Bigfoot » pour Veo 3 décortiqué par Ai For Real Life suit le même ordre, avec des blocs « Lighting: … Camera: … Audio: … » et une fin « Voice is low, gravelly. No background music. No subtitles » ([Ai For Real Life](https://ai-for-real-life.beehiiv.com/p/master-google-veo-3-prompts-the-bigfoot-video-breakdown-new-post)).

### La réplique s'attache à un geste, et le français reste le point faible

Les règles de dialogue sont les plus précises de toute la doctrine. Kling, par la voix de fal, en publie quatre, qu'Alibaba reprend presque mot pour mot pour Wan : des étiquettes de personnage uniques et constantes, sans pronoms ni synonymes ; le geste avant la réplique ; une voix et une émotion propres à chaque personnage ; des mots de liaison comme « Immediately » pour séparer les tours de parole ([fal](https://blog.fal.ai/kling-3-0-prompting-guide) ; [Alibaba Cloud](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt)). Sora demande de « label speakers consistently and use alternating turns ». Il donne surtout **la seule règle de durée publiée par un éditeur** : « a 4-second shot will usually accommodate one or two short exchanges, while an 8-second clip can support a few more. Long, complex speeches are unlikely to sync well » ([OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)). Replicate ajoute qu'une réplique trop courte (« Hello, I'm John ») produit du charabia et qu'une trop longue est récitée en accéléré ([Replicate](https://replicate.com/blog/using-and-prompting-veo-3)). PixPretty conseille de rester sous 15 mots par plan de nourriture parlante ([PixPretty](https://pixpretty.tenorshare.ai/ai-generator/viral-talking-food-video-ai-prompts.html)). Magic Hour conseille un seul locuteur principal par plan et, si l'attribution des répliques échoue, de « generate each line as a separate shot and assemble the exchange in an editor » ([Magic Hour](https://magichour.ai/blog/how-to-prompt-for-speaking-in-veo-3)). C'est exactement notre règle « un plan, une réplique, un personnage ».

Lightricks va plus loin pour LTX-2.3 : « write one phrase of dialogue at a time, then a short acting direction, then the next phrase. Don't quote a full sentence. Don't separate the dialogue from the acting into different paragraphs ». Sans ce découpage, prévient le guide, « the timing collapses » : le modèle accélère la réplique ou remplit le vide par des gestes qui la contredisent. Il fixe aussi une limite à l'excès inverse : « One direction per beat is the working limit » ([LTX](https://ltx.io/blog/directing-dialogue-and-acting)). Une astuce de prononciation complète le tout : écrire les noms propres phonétiquement quand le modèle les écorche ([Replicate](https://replicate.com/blog/using-and-prompting-veo-3)).

**La langue est le maillon faible pour une série en français.** Le guide officiel de Kling 3.0 est explicite : « Video 3.0 supports dialogue output in five languages: Chinese, English, Japanese, Korean, and Spanish… If dialogue is entered in a language other than those listed above, the model will translate it into English » ([Kling](https://kling.ai/quickstart/klingai-video-3-model-user-guide)). Seedance 1.5 Pro liste le mandarin et ses dialectes, l'anglais, le japonais, le coréen, l'espagnol et l'indonésien, sans le français ([BytePlus](https://docs.byteplus.com/en/docs/ModelArk/seedance-1-5-pro)). Pour Seedance 2.0, une source tierce parle de « 8+ languages » sans confirmer ni exclure le français ([Cutout.pro](https://www.cutout.pro/learn/blog-seedance-2-0-audio-guide/)). Veo 3.1 et Omni Flash écrivent : « English (EN) is fully supported, but other languages have not been evaluated, so they may work but results can vary » ([Gemini API](https://ai.google.dev/gemini-api/docs/veo)). LTX demande de « mention the language and accent you would like the character to have » ([LTX](https://ltx.io/blog/prompting-guide-for-ltx-2)). Mais la fiche Hugging Face de LTX-2.3 liste le français dans ses métadonnées tout en écrivant « Language(s): English » dans son texte ([Hugging Face](https://huggingface.co/Lightricks/LTX-2.3)), et un fil du forum signale des problèmes de dialogue ([forum Hugging Face](https://discuss.huggingface.co/t/ltx-2-3-problem-with-dialogs/176649)). Chez nous, le français tient pourtant en pratique. Sur les 24 plans de notre épisode 1 où le modèle (LTX-2.3 ou Agnes) prononçait lui-même la réplique, la meilleure prise a été reconnue par whisper avec une similarité d'au moins 0,92 avec le script dans 21 cas, et de 0,79 au pire (fichier de contrôle `episodes/01_la_bague/state.json`). Ce contrôle mesure les mots, pas l'accent ni le naturel, et aucun éditeur ne garantit ce résultat d'une version à l'autre. Les exemples multilingues officiels donnent la marche à suivre : **la mise en scène en anglais, la réplique dans sa langue, et la langue nommée juste avant**. Exemple chez Kling : « Female tourist (speaking slightly slowly, with an awkward accent, in Spanish): Disculpe, ¿dónde está la plaza mayor? » ([Kling](https://kling.ai/quickstart/klingai-video-3-model-user-guide)). Un module tiers pour Agnes traduit d'ailleurs en anglais tout prompt non anglais « for stable video generation output » ([GitHub agnes-ai-skill](https://github.com/jomeswang/agnes-ai-skill)).

Reste la querelle des guillemets, liée aux faux sous-titres. Replicate affirme que ces sous-titres viennent des vidéos d'entraînement sous-titrées et conseille d'écrire la parole après deux-points, sans guillemets (« A guy says: My name is Ben »), puis de répéter « No subtitles » si besoin ([Replicate](https://replicate.com/blog/using-and-prompting-veo-3)). DG Mastery dit la même chose ([DG Mastery](https://dgmastery.beehiiv.com/p/how-to-structure-veo-3-prompts-with-dialogue-for-viral-ai-content-b8759051fa573851)). Le guide Vertex de Google écrit lui aussi la réplique après deux-points sans guillemets (« The seasoned detective says: Your story has holes »), alors que le blog Veo 3.1 et l'API Gemini demandent des guillemets ([Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide) ; [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)). Kling, Seedance 2.0 et LTX veulent des guillemets ([Replicate Seedance 2.0](https://replicate.com/bytedance/seedance-2.0/readme)). Aucun test contrôlé ne tranche. Pour nous, la question est réglée par l'expérience : **Agnes v2.0 a incrusté de faux sous-titres dans 3 clips sur 3, avec ou sans guillemets**. On suit donc la doc de chaque moteur (guillemets pour LTX) et on masque la bande au montage.

### Longueur, JSON et interdits : trois querelles et leur arbitrage

La longueur divise les éditeurs. Les plafonds connus vont de **1 024 jetons pour Veo 3.1** ([Gemini API](https://ai.google.dev/gemini-api/docs/veo)) à **7 000 caractères pour MiniMax H3** ([MiniMax](https://platform.minimax.io/docs/guides/video-generation)). Le README de LTX-2 dit « Keep within 200 words » ([GitHub LTX-2](https://github.com/Lightricks/LTX-2)), et le blog LTX attend « 4 to 8 descriptive sentences » ([LTX](https://ltx.io/blog/prompting-guide-for-ltx-2)). Le guide de LTX-2.3 affirme au contraire que « longer, more descriptive prompts consistently outperform short ones on LTX-2.3, because the model has more anchors to align the generation against » ([LTX](https://ltx.io/blog/directing-dialogue-and-acting)). Sora tient la position inverse : « Longer, more detailed prompts restrict the model's creativity. It will try to follow your guidance, but might not always do so reliably ». Il conseille, quand un plan rate, de « strip it back: freeze the camera, simplify the action, clear the background » ([OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)). La contradiction se résout bien : la longueur aide quand elle ajoute des repères (traits figés du personnage, contraintes de continuité, son explicite) et nuit quand elle ajoute des actions, des personnages ou des consignes simultanés. Le guide LTX-2 le dit lui-même : « The more actions/ characters/ instructions you add, the higher the chance some of them won't be seen in the output » ([LTX](https://ltx.io/blog/prompting-guide-for-ltx-2)). Nous en tirons une cible, qui reste une déduction : pour un plan de Rue des Fruits, **120 à 180 mots** gardent tous les repères sans dépasser les 200 mots du README.

**Aucun éditeur ne recommande le JSON.** Tous les exemples officiels sont en prose ou en blocs de texte étiquetés, et LTX exige un paragraphe unique. Les défenseurs du JSON y voient « a shot list for AI video that helps you maintain consistency across multiple clips » ([Artlist](https://artlist.io/blog/veo-3-json-prompts/)). Les sceptiques répondent que « it doesn't matter much at all, because Veo often does whatever it wants anyway » ([The Creative Possible](https://creativepossible.substack.com/p/should-you-prompt-in-json)). Le guide LTX-2.3 prévient que son nouveau module de lecture du texte « doesn't ignore the noise » ([LTX](https://ltx.io/blog/directing-dialogue-and-acting)) : des accolades ou des balises envoyées au modèle risquent d'être lues comme du contenu. L'arbitrage est simple. Le JSON sert de format de travail, comme le plan multi-scènes de Tenten avec sa liste `continuity.characters` ([Tenten](https://developer.tenten.co/veo-331-pro-json-prompting-step-by-step)) ou notre `episode.json`, puis on le transforme en prose avant de l'envoyer.

Les interdits ne marchent pas comme on le croit. Google déconseille les tournures « no walls » et recommande de lister dans le champ négatif des noms nus (« wall, frame ») ([Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)). Le blog Veo 3.1 conseille de décrire positivement ce qu'on veut, « a desolate landscape with no buildings or roads » ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)). Omni Flash n'a pas de champ négatif du tout et demande d'écrire « Do not do X » dans le prompt ([Gemini API](https://ai.google.dev/gemini-api/docs/omni)). Wan utilise des phrases courtes dans le texte : « No dialogue. », « No background music. », « Generate single shot. » ([Alibaba Cloud](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt)). La pipeline ouverte de LTX, elle, a un vrai champ `negative_prompt`, dont l'exemple officiel est « shaky, glitchy, low quality, worst quality, deformed, distorted, disfigured, motion smear, motion artifacts, fused fingers, bad anatomy, weird hand, ugly, transition, static. » ([Hugging Face LTX-2](https://huggingface.co/Lightricks/LTX-2)). Le cadre méta de snubroot propose une liste centrée sur le texte : « subtitles, captions, watermark, text overlays, words on screen, logo, blurry footage, low resolution, artifacts, distorted hands, compression noise, camera shake » ([GitHub snubroot](https://github.com/snubroot/Veo-3-Meta-Framework)). Les négatifs restent faibles. MIT Technology Review a montré que Veo 3 ajoutait des sous-titres incompréhensibles « even when the prompts it's been given explicitly ask for no captions or subtitles to be added » ([MIT Technology Review](https://www.technologyreview.com/2025/07/15/1120156/googles-generative-video-model-veo-3-has-a-subtitles-problem/)). Le recours de dernier ressort consiste à recadrer les 10 à 15 % du bas de l'image ([Yapper](https://yapper.so/articles/remove-veo3-subtitles)) ou, comme nous, à flouter la bande et à poser nos sous-titres dessus.

Le son mérite une consigne explicite, car les réglages par défaut diffèrent. Seedance 1.5 « automatically generates background music that matches the prompt » ([BytePlus](https://docs.byteplus.com/en/docs/ModelArk/seedance-1-5-pro)). Wan choisit une musique tant qu'on n'écrit pas « No background music. » ([Alibaba Cloud](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt)). Omni Flash génère sa propre bande-son ([Gemini API](https://ai.google.dev/gemini-api/docs/omni)). LTX-2.3, sans consigne, rend un son plat : « A prompt without any audio direction leaves the model to default to a flat studio sound ». Il veut la consigne sonore en dernier, avec quatre éléments : l'espace acoustique, la texture de la voix, la forme des silences et les bruits d'ambiance ([LTX](https://ltx.io/blog/directing-dialogue-and-acting)). Préciser l'ambiance évite aussi les rires enregistrés ou les voix parasites, par exemple « Audio: quiet office ambiance, no audience sounds » ([GitHub snubroot](https://github.com/snubroot/Veo-3-Prompting-Guide)).

Le prompt d'un plan image → vidéo, enfin, ne doit pas redécrire l'image. Alibaba l'écrit sans détour : « The image defines the entity, scene, and style. Your prompt should focus on motion and camera movements » ([Alibaba Cloud](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt)). Sora et xAI disent que l'image est la première image et que le texte décrit « what happens next » ([OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) ; [xAI](https://docs.x.ai/developers/model-capabilities/video/overview)). Flashloop conseille des consignes de mouvement de 3 à 5 secondes comme « Slow push-in on the character's face as tears form in their eyes » ([Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)). L'exemple I2V de Veo restaure pourtant la scène en une phrase avant le mouvement ([Gemini API](https://ai.google.dev/gemini-api/docs/veo)). La redite courte est donc tolérée, et elle aide à attribuer la bonne bouche quand le modèle doit savoir qui parle. Notre gabarit garde le bloc personnage pour cette raison, et parce que nos essais ont montré qu'Agnes confondait les personnages dès qu'on les désignait mal.

## La constance se fabrique hors du prompt

### Une phrase d'identité figée, un accessoire signature, jamais un prénom seul

Les créateurs expérimentés suivent tous la même pile : fixer la distribution avant d'animer, recopier le même texte d'apparence dans chaque plan, fabriquer une image clé par plan puis l'animer, et assembler au montage ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1) ; [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)). Le texte d'apparence doit être recopié à la lettre. UlazAI conseille d'écrire « one sentence that names age, hair, outfit and one distinguishing detail », de la coller telle quelle partout et de ne changer que l'action, la caméra et le lieu ([UlazAI](https://ulazai.com/character-consistency/)). Un testeur qui a dépensé 400 $ en essais Veo 3 a constaté que « realistic bigfoot » restait stable d'un prompt à l'autre, mais que **le simple ajout de « wearing glasses » cassait l'identité** ([Alejandro Dinsmore](https://alejandrodinsmore.substack.com/p/deep-dive-veo-3-i-spent-400-testing)). Le modèle n'a pas non plus de mémoire : lui demander « the same characters as the last scene » ne marche pas ([Tom's Guide](https://www.tomsguide.com/ai/i-turned-my-chaotic-family-life-into-a-sitcom-with-veo-3-heres-what-worked-and-what-didnt)). Pour changer de tenue, snubroot reprend les mots du visage et remplace seulement les vêtements : « Dr. Jennifer Walsh, the same 35-year-old pediatrician with short brown hair in a bob cut and kind green eyes, now wearing a casual green sweater and dark jeans... » ([GitHub snubroot](https://github.com/snubroot/Veo-3-Prompting-Guide)). C'est déjà la forme de nos fiches de tenue (« the same woman, same face… now wearing… »).

Flashloop ajoute deux outils propres aux feuilletons de fruits. Il faut d'abord **un accessoire signature par personnage** (perles, rouge à lèvres, montre en or) qui sert d'ancre visuelle. Il faut ensuite 5 à 10 images de référence par personnage, dont on retient une seule, canonique ([Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)). Pour des fruits, l'accessoire compte double, puisqu'une feuille manquante ou une couleur décalée est la dérive la plus visible. Le projet libre drama-skills formalise ce principe en « verrou de continuité » : une formule unique, « pasted into every affected prompt unchanged », par exemple « Continuity lock: LOCK-JIANGCHEN-DRESS "Jiang Chen's pine-green service uniform" […] · lock phrase: pine-green lapel service jacket ». Un script vérifie ensuite que chaque prompt concerné contient bien la formule ([drama-skills](https://github.com/zenstory-ai/drama-skills/blob/main/README_EN.md)).

Les sources se contredisent sur les prénoms, et la contradiction se résout proprement. Flashloop dit de décrire les personnages par leur apparence « because the AI doesn't know character names » ([Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)). Aicut et AI Fruit Video disent au contraire de toujours employer le même nom ([Aicut](https://www.aicut.pro/how-to/cheating-fruits) ; [aifruitvideo.com](https://aifruitvideo.com/tools/ai-fruit-drama)). Les deux ont raison selon l'outil. Un nom ne fonctionne que si une image de référence enregistrée porte l'identité : un identifiant Sora, un `@élément` Kling, un `@character` dans huobao-drama ([huobao-drama](https://github.com/chatfire-AI/huobao-drama)). En texte seul ou en image → vidéo simple, il faut décrire. Nos essais du 8 octobre l'ont confirmé à nos dépens : appelé par son nom, le croissant a été dessiné comme une baguette avec le visage du croissant. **Dans nos prompts, le prénom n'apparaît donc jamais seul** ; il ne sert qu'à l'équipe et à la bible. La longueur du bloc n'est mesurée par personne. L'exemple de snubroot fait une cinquantaine de mots ([GitHub snubroot](https://github.com/snubroot/Veo-3-Prompting-Guide)), ce qui place la bonne longueur autour de **30 à 60 mots**, déduction tirée des exemples publiés.

### Chaque modèle a son mécanisme de référence, et le libre en a deux

Les modèles payants ont tous une porte d'entrée pour les images de référence. Pour les fruits, c'est la méthode la plus robuste, car aucun texte ne fixe un visage de cerise précis.

| Modèle | Mécanisme | Limites publiées | Voix liée au personnage | Accès |
|---|---|---|---|---|
| Veo 3.1 | « Ingredients » : on cite les images par rôle (« Using the provided images for the detective, the woman, and the office setting… ») | 3 images au plus, durée forcée à 8 s, absent de Veo 3.1 Lite | non | payant ([Gemini API](https://ai.google.dev/gemini-api/docs/veo) ; [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)) |
| Gemini Omni Flash | balises `<IMAGE_REF_N>`, `<VIDEO_REF_N>` | 3 clips de 3 s au plus ; pas de référence audio | non | payant ([Gemini API](https://ai.google.dev/gemini-api/docs/omni)) |
| Kling 3.0 | « Elements » appelés par `@Nom` | 2 à 4 images par élément | **oui** : extrait parlé de 5 à 30 s ou voix de bibliothèque | payant ([Kling](https://kling.ai/quickstart/klingai-element-library-3-user-guide)) |
| Grok Imagine 1.5 | `<IMAGE_0>`, `<AUDIO_0>`, « The woman from <IMAGE_0> is Lena » | 14 images, 3 voix ; voix personnelles réservées aux partenaires ; 720p et 15 s | **oui** | payant ([xAI](https://docs.x.ai/developers/model-capabilities/video/overview)) |
| Seedance 2.0 | `[Image1]`, `[Video1]`, `[Audio1]` | 9 images, 3 vidéos, 3 fichiers audio | par référence audio | payant ([Replicate](https://replicate.com/bytedance/seedance-2.0/readme)) |
| Wan 2.6 à 3.0 | référence → vidéo, « character1 » | 3 personnages ; « preserves… voice timbre (if present) » | par référence | payant via API ([Alibaba Cloud](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt)) |
| LTX-2.5 (libre) | IC-LoRA « Ingredients » : planche personnages et décor sur fond noir | clips d'environ 5 s, GPU | non | gratuit, poids ouverts ([Hugging Face](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Ingredients)) |
| LTX-2.3 (libre) | LoRA de ressemblance par personnage | entraînement « less than an hour in many settings » | « likeness (sound+appearance) » | gratuit, GPU ([Hugging Face](https://huggingface.co/Lightricks/LTX-2.3)) |

Côté libre, les autres briques servent surtout à fabriquer les images clés. Qwen-Image-Edit 2509 accepte une à trois images en entrée ([RunComfy](https://www.runcomfy.com/comfyui-workflows/qwen-image-edit-2509-in-comfyui-multi-image-merge-edit)) et sert à constituer des jeux d'images cohérents pour entraîner un LoRA ([WeirdWonderfulAI](https://weirdwonderfulai.art/comfyui/qwen-image-edit-can-create-character-consistent-lora-dataset/)). StoryDiffusion garde un même personnage sur une suite d'images (licence Apache-2.0, [GitHub](https://github.com/HVision-NKU/StoryDiffusion)), et le flux Wan 2.2 interpole entre une première et une dernière image ([RunComfy](https://www.runcomfy.com/comfyui-workflows/comfyui-wan2-2-fun-inp-workflow-first-to-last-frame-interpolation)). Notre propre règle, née des essais, reste la plus simple : **le décor d'abord, puis un seul personnage ajouté par passe avec sa fiche comme référence**, car deux personnages dans une même passe se mélangent.

Deux règles d'usage reviennent dans les guides. La première : ne jamais réinjecter une image qui a dérivé. UlazAI demande de revenir à l'image source plutôt que de repartir du rendu fautif ([UlazAI](https://ulazai.com/character-consistency/)). L'enchaînement « dernière image du plan A = première image du plan B » ne vaut donc qu'à l'intérieur d'une même action continue ; Veo lui-même bâtit ses extensions à partir de la seule dernière seconde, soit 24 images ([Gemini API](https://ai.google.dev/gemini-api/docs/veo)). La seconde : générer plusieurs candidats et choisir automatiquement. ViMax produit deux images clés par plan et laisse un modèle de vision choisir ([GitHub ViMax](https://github.com/HKUDS/ViMax)), drama-skills vérifie ses verrous par script ([drama-skills](https://github.com/zenstory-ai/drama-skills/blob/main/README_EN.md)), et Sider conseille un tableau de continuité (personnage, tenue, accessoires, objectif, lumière) recopié de plan en plan ([Sider](https://sider.ai/blog/ai-tools/how-veo-3_1-maintains-character-scene-consistency-in-ai-video)). Notre juge visuel et notre contrôle whisper jouent déjà ce rôle.

### La voix, seul problème que nos voix clonées règlent déjà

Garder la même voix d'un plan à l'autre est le problème que les modèles à audio natif résolvent le moins bien. Google ne documente aucun réglage de constance vocale, et une voix ne se prolonge dans une extension Veo que si elle est présente dans la dernière seconde ([Gemini API](https://ai.google.dev/gemini-api/docs/veo)). Sora ne dit rien sur le sujet ([OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)). Trois parades existent. La première consiste à recopier une description fixe de la voix dans chaque prompt, « quiet, high-pitched, slightly hoarse » par exemple ([UlazAI](https://ulazai.com/character-consistency/)) : c'est bon marché mais peu fiable. La deuxième lie une voix au personnage dans l'outil, ce que permettent Kling (extrait de 5 à 30 s), Grok, Wan, Seedance et MiniMax, tous payants. La troisième remplace la voix après coup. Un créateur génère ses clips Veo puis les passe dans le changeur de voix d'ElevenLabs « to standardize them to one voice profile » ([AI for Real Life](https://ai-for-real-life.beehiiv.com/p/the-secret-to-consistent-characters-in-veo-3-and-how-to-fix-the-voices-too)), un usage que la doc d'ElevenLabs décrit comme « consistent character voices across multiple languages and recording sessions » ([ElevenLabs](https://elevenlabs.io/docs/overview/capabilities/voice-changer)). D'autres retirent la voix générée et doublent avec une voix clonée ([MindStudio](https://www.mindstudio.ai/blog/elevenlabs-voice-cloning-replace-ai-generated-voices)).

Nous pratiquons déjà la troisième voie, avec des voix clonées pour chaque personnage (Chatterbox pour Cerise, Citron, Pêche et Kiwi, une voix décrite en texte pour Mamie Prune). Le clip est ensuite recalé sur la voix, ou animé directement à partir d'elle, un mode « audio-driven » que l'hébergeur Runware documente pour LTX-2.5 Pro ([Runware](https://runware.ai/docs/models/lightricks-ltx-2-5-pro/guides/audio-driven)). **Tout ce que les guides disent sur la constance du timbre ne nous concerne donc pas.** La consigne de voix garde pourtant un rôle dans nos prompts : elle règle l'énergie du jeu et la forme de la bouche. Elle n'a pas à décrire un timbre précis, qui ne sera jamais entendu. Nos essais l'ont montré : « very deep, gravelly old man » n'a jamais donné de voix grave.

## Une histoire de 75 secondes se découpe en battements d'une réplique

### Deux matrices ont fait les millions : le mélo conjugal et la téléréalité parodiée

Le genre est né le 28 février 2026 avec la « sad fruit story » de @trombonechef ([Know Your Meme](https://knowyourmeme.com/memes/cheating-ai-fruit)). Une fraise qui « travaille tard » trompe son mari avec son patron aubergine ; à l'accouchement, le bébé est une aubergine. La partie 1 a dépassé 2,9 millions de vues. **La partie 2, publiée dès le lendemain, en a fait plus de 24 millions** : le mari part avec une orange, l'épouse en deux jours et met dehors sa femme et le bébé. La partie 3 (le patron refuse d'aider, la fraise achète une arme) a fait 4,9 millions, et la série comptait douze épisodes à la mi-mars ([Know Your Meme](https://knowyourmeme.com/memes/cheating-ai-fruit)). Le Daily Dot cite d'autres prémisses à succès, comme une banane qui tient un bébé et s'écrie « This is a pear! Are you cheating on me? » ([Daily Dot](https://dailydot.com/ai-slop-videos-of-cheating-fruit-are-taking-over-tiktok)). Une leçon de construction se dégage de ces exemples : **l'espèce du fruit porte le rebondissement**. Le bébé qui ressemble à l'amant se lit en une image, sans une ligne d'explication. Pour Rue des Fruits, le fruit lui-même peut servir d'indice ou de chute, comme le « Un citron, ma chérie… Ça finit toujours pressé » de Mamie Prune le fait déjà.

La seconde matrice est la parodie de téléréalité. *Fruit Love Island* parodiait *Love Island* : une villa, des épreuves, un « Casa Amor » en plusieurs parties, des votes du public par formulaire Google, et des épisodes moyens de plus de 10 millions de vues ([Wikipedia](https://en.wikipedia.org/wiki/Fruit_Love_Island)). Chaque nouveau candidat arrivait avec sa ville d'origine, comme dans l'émission : Passiona « from Massachusetts », Limeyra « from Miami » ([NBC News](https://www.nbcnews.com/pop-culture/viral/ai-fruit-love-island-tiktok-slop-popularity-rcna264946)). Un universitaire y voit « the video version of fan fiction », facile à reproduire parce que les archétypes de l'émission sont simples ([NBC News](https://www.nbcnews.com/pop-culture/viral/ai-fruit-love-island-tiktok-slop-popularity-rcna264946)). En France, *L'Île de la Skibidi Tentafruit* a rassemblé près de 3 millions d'abonnés et environ 25 millions de mentions « j'aime » en 12 épisodes, avec un « nouveau tentateur » à l'épisode 9 et des marques (Oasis, Danette, Free, Picard) qui se sont invitées dans l'intrigue ([Presse-citron](https://www.presse-citron.net/cest-nul-mais-tout-le-monde-regarde-les-fruits-ia-explosent-les-compteurs-sur-tiktok/)). Elle a dépassé 266 millions de vues en moins de trois semaines ([franceinfo](https://www.franceinfo.fr/replay-radio/le-vrai-du-faux-junior/ile-de-la-skibidi-tentafruit-non-le-createur-n-a-pas-ete-condamne-a-cinq-ans-de-prison_7940213.html)). WOO appelle cette méthode du « hijacking culturel » : prendre un format que le public connaît déjà et y injecter de l'absurde ([WOO Paris](https://www.woo.paris/blog/lile-de-la-skibidi-tenta-fruit-la-tele-realite-generee-par-ia-qui-explose-tout)).

### Réplique choc à 0 seconde, escalade toutes les 10, coupure nette

Les guides donnent des structures d'épisode compatibles entre elles. Flashloop, un vendeur, propose « recap → rising tension → dramatic peak → cliffhanger », avec un pic du type « You're not the father! » et une consigne finale : « Never resolve everything ». La carte de fin annonce « Part [X] tomorrow... », et les sous-titres sont obligatoires parce que beaucoup regardent sans le son ([Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)). Aicut découpe en cinq scènes : moment normal, soupçon, découverte, confrontation, chute ([Aicut](https://www.aicut.pro/how-to/cheating-fruits)). AI Fruit Video condense un plan en une phrase à trous ([aifruitvideo.com](https://aifruitvideo.com/tools/ai-fruit-drama)) :

> "[fruit character] wants [visible goal], but [conflict]. Show [emotion change], [action], and "short dialogue" in [setting]. Use [camera + light], then end on [reaction or cliffhanger]."

Deux guides donnent les règles de rétention les plus utiles. Le premier, publié sur qwe.edu.pl, plante « a major hook every 45–60 seconds » et termine chaque épisode sur un cliffhanger qui se résout « in the first 10 seconds of the next », avec un nouveau crochet dans les cinq dernières secondes. Il pose aussi la règle de découpage la plus nette du corpus : « Each beat = one shot = one AI generation ». Il prévient enfin qu'un script en prose donne des plans de longueurs incohérentes (« some generate 3 seconds of footage, some 12. Pacing collapses ») et résume le mixage en une ligne : « Music low, dialogue loud, cliffhanger sting on the last frame » ([qwe.edu.pl](https://www.qwe.edu.pl/tutorial/short-dramas-ai-beginners-guide/)). Le second, celui d'invideo, prévoit « one dramatic beat per episode » de 60 à 120 secondes et exige que « the shot list should already know which shot is the cliffhanger » ([invideo](https://invideo.io/blog/how-to-make-ai-micro-drama/)).

Les chiffres de durée des guides de vendeurs sous-estiment la densité réelle des histoires françaises. Flashloop parle de 4 à 6 scènes de 3 à 5 secondes et de 80 à 90 caractères de voix par scène, ce qui ne fait que 20 à 48 secondes pour un épisode censé durer une à deux minutes ([Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)). Notre analyse interne du 8 octobre, menée sur 22 vidéos d'histoires IA dont 19 en français (fichier `orbeo_studio/ligne_shorts/references/formule.md`), donne une autre image. Ces vidéos durent typiquement **75 secondes**, et la première réplique tombe à 0,0 s dans 14 vidéos sur 17. La parole occupe typiquement 94 % du temps, à raison d'**une réplique toutes les 2,5 secondes** et d'environ 2,7 mots par seconde. Les « scènes » des vendeurs sont donc des scènes d'histoire, et chacune se découpe en plusieurs plans d'une réplique : notre épisode 1 compte 29 plans. Cette grammaire tombe bien, car c'est celle où nos outils gratuits réussissent le mieux (un personnage, gros plan, réplique de 4 secondes au plus).

Le méta-prompt d'Aicut donne les meilleures consignes d'écriture des répliques. Ses règles valent mot pour mot pour nous ([aicut.pages.dev](https://aicut.pages.dev/)) :

> "Dialogue rules:
> - keep lines short
> - keep lines sharp
> - keep lines emotionally clear
> - keep lines instantly understandable
> - do not write weak generic dialogue
> - if silence is stronger, keep the scene silent
> [...]
> LIP-SYNC RULE:
> - only the active speaker's mouth moves
> - no mouth movement from silent characters
> - no accidental background talking"

### Les thèmes qui retiennent, et ceux qui font retirer les vidéos

Flashloop classe les thèmes ainsi : la tromperie en tête, puis les grossesses inattendues, les guerres d'héritage, les vengeances sur plusieurs épisodes et les identités secrètes. Ses exemples les plus vus se passent dans des décors de richesse : la brocolie enceinte dans un penthouse de Manhattan (24,5 millions de vues), un raisin méchant à un gala de charité (9 millions). Ce classement est celui d'un vendeur ([Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos)). En Chine, les micro-dramas d'animaux exploitent les drames de palais, les trahisons au bureau et les ascensions sociales ([CGTN](https://news.cgtn.com/news/2026-03-20/AI-Influence-Pet-and-fruit-microdramas-take-the-internet-by-storm-1LEUvn7BBOE/p.html)). Notre échantillon français ajoute la revanche de l'humilié, le riche déguisé qui teste les autres et le danger caché. Il retrouve quatre constantes : un méchant clair, une victime à qui l'on s'attache, un enjeu chiffré et une fin coupée net.

Ces thèmes ont un coût de réputation. La presse a qualifié ces séries de « slop », de racistes et de misogynes, et certains épisodes montraient des violences conjugales, des agressions sexuelles et des meurtres ([Daily Dot](https://dailydot.com/ai-slop-videos-of-cheating-fruit-are-taking-over-tiktok) ; [IOL](https://iol.co.za/saturday-star/2026-04-11-ai-fruit-dramas-take-over-tiktok/) ; [Safe on Social](https://www.safeonsocial.com/post/the-ai-fruit-drama-is-not-a-joke-it-is-a-case-study-in-algorithmic-misogyny)). *Fruit Love Island* a cessé sa production le 28 mars 2026, alors que TikTok retirait des épisodes ([Wikipedia](https://en.wikipedia.org/wiki/Fruit_Love_Island)). Une créatrice, Joy Ofodu, a dit que la série s'inspirait de ses propres vidéos de fruits ([AOL](https://www.aol.com/articles/black-creator-says-ai-fruit-164743347.html)). Garder la trahison et la revanche, sans arme, sans agression et sans copie scène à scène d'une vidéo existante, protège à la fois le compte et les futurs partenariats. Le conseil « Keep the story role. Change the fruit » d'Aicut, qui consiste à refaire une vidéo virale en changeant les fruits ([aicut.pages.dev](https://aicut.pages.dev/)), va contre la règle de TikTok sur le contenu non original ([ContentIQ](https://contentiq.media/rules/tiktok)). Pour être payé par Creator Rewards, il faut aussi que chaque épisode dure **plus d'une minute** ([ShortsFast](https://shortsfast.com/blog/tiktok-creator-rewards-eligibility-2026/)).

### Octobre 2026 : beaucoup de signaux, aucune vague documentée

**Aucune source fiable ne décrit un nouveau format d'histoire IA lancé en septembre ou en octobre 2026.** Toutes les recherches ramènent à la vague de février à avril. Les signaux récents existent mais restent épars. Le classement SocialPeta du 13 au 19 juillet 2026 range le « mélodrame de fruits personnifiés » parmi les trois thèmes marquants de la semaine, sur environ 43 200 micro-dramas actifs ; seul un extrait de recherche a pu être lu ([SocialPeta](https://socialpeta.com/en/blog/short-drama-weekly-ranking-43k-titles-compete-as-ai-dramas-rise-and-fruit-themed-melodramas-expand-globally)). En Chine, les créateurs sont passés des fruits aux objets personnifiés (téléphones, AirPods, bouteilles d'eau, thé au lait, bijoux) dans des histoires de 30 secondes de divorce, de tromperie et de grossesse ([36Kr](https://www.36kr.com/p/3785208441598728)). En France, TF1+ a lancé en juin « Skibidi Exfruit » avec les créateurs de Tentafruit, publié chaque soir à 19 h, qui a fait 4,7 millions de vues en 72 heures ([Le Tribunal du Net](https://www.letribunaldunet.fr/tv/tf1-skibidi-exfruit-telerealite-ia-tiktok.html)). À Singapour, l'IMDA et TikTok ont lancé le 1er octobre un programme de micro-dramas de 50 à 100 épisodes faits avec Seedance 2.5 ([TNGlobal](https://technode.global/2026/10/01/imda-partners-tiktok-to-develop-local-microdrama-expertise-and-fuel-a-new-pipeline-of-original-ip)). Notre échantillon du 8 octobre confirme que le genre vit encore : des comptes inconnus y font 1 à 4 millions de vues par épisode, et les séries à héros récurrent (Dragono, « Kiwi et Fraise ») y réussissent le mieux. Le funk brésilien y domine (« TREND DAS FRUTAS »), et « Камин » accompagne les histoires tristes.

La tendance la plus nette concerne les outils, pas les histoires. **En 2026, le multi-plans dans une seule génération est devenu la norme des modèles payants** : Kling 3.0 jusqu'à 15 secondes et six plans ([fal](https://blog.fal.ai/kling-3-0-prompting-guide)), Seedance 2.0, Wan 2.6 et suivants avec « Shot 1 [0–3 s] » ([Alibaba Cloud](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt)), Omni Flash qui coupe par défaut ([Gemini API](https://ai.google.dev/gemini-api/docs/omni)). S'y ajoute la voix attachée au personnage (Kling, Grok 1.5). Du côté gratuit, seul LTX-2.5 annonce le multi-plans natif, et seulement d'après des sources tierces ([deAPI](https://deapi.ai/blog/ltx-2-5-prompting-guide-multi-shot-scenes-native-audio-and-prompts-that-actually-cut)).

## Le tri pour notre chaîne gratuite : LTX, Agnes et voix clonées

Notre chaîne actuelle enchaîne trois briques. LTX-2.3 tourne sur un Space Hugging Face, LTX-2 TURBO peut animer un plan à partir de notre fichier de voix, et Agnes 2.5-flash sert de secours. Les voix clonées sont ajoutées après coup, et chaque clip passe par whisper et par le juge visuel. Beaucoup de conseils lus plus haut visent des modèles payants et n'ont pas d'effet ici. Le tableau trie ce qui s'applique ; « à tester » signale l'absence de documentation et d'essai.

| Conseil | D'où il vient | LTX-2.x (Hugging Face) | Agnes 2.5-flash | Effet de nos voix ajoutées après | Réservé aux modèles payants ? |
|---|---|---|---|---|---|
| Un seul paragraphe au présent, 4 à 8 phrases, 200 mots au plus | [README LTX-2](https://github.com/Lightricks/LTX-2), [blog LTX](https://ltx.io/blog/prompting-guide-for-ltx-2) | **Oui, consigne officielle** | À tester : aucune doc, mais même règle d'images en 8n+1 que LTX ([passerelle tierce](https://agnes-compatible-gateway.zo.deno.net/)), indice faible d'une parenté | aucun | Non. Sora et xAI préfèrent des blocs étiquetés |
| Style nommé en premier | [LTX](https://ltx.io/blog/prompting-guide-for-ltx-2), [OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) | Oui | Probablement | aucun | Non |
| Mise en scène en anglais, réplique française entre guillemets, langue nommée | [LTX](https://ltx.io/blog/prompting-guide-for-ltx-2), [Kling](https://kling.ai/quickstart/klingai-video-3-model-user-guide) | Oui ; le français n'est pas garanti par la fiche, mais il tient sur notre épisode 1 | Oui d'après nos essais ; à revérifier sur 2.5-flash | La réplique anime les lèvres et le jeu ; le timbre vient du clone | Kling 3.0 traduit le français en anglais ; Seedance 1.5 n'a pas de français |
| Réplique coupée en segments, une indication de jeu entre deux | [LTX-2.3](https://ltx.io/blog/directing-dialogue-and-acting) | **Oui** | À tester | Couper aux mêmes ponctuations que les pauses de nos voix, pour que le recalage reste simple | Non |
| Consigne sonore à la fin, « no music » | [LTX-2.3](https://ltx.io/blog/directing-dialogue-and-acting), [Runware](https://runware.ai/docs/models/lightricks-ltx-2-5-pro/guides/native-audio.md) | Oui (sinon son plat ou musique ajoutée) | À garder | La voix est remplacée ; l'ambiance peut servir | Seedance, Wan et Omni ajoutent de la musique par défaut |
| Caméra fixe, « hold the frame during pauses », pas de panoramique pendant la parole | [LTX-2.3](https://ltx.io/blog/directing-dialogue-and-acting) | Oui | Oui : nos essais montrent zoom et recomposition sans cette consigne | aucun | Non |
| Interdits en noms nus dans un champ séparé | [Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide), [LTX-2](https://huggingface.co/Lightricks/LTX-2) | Oui, champ `negative_prompt` | Notre client l'envoie ; sans effet sur les faux sous-titres (3 sur 3) | aucun | Omni n'a pas de champ ; non vérifié pour Kling, Seedance et Grok |
| Deux-points sans guillemets contre les sous-titres | [Replicate](https://replicate.com/blog/using-and-prompting-veo-3) | Contraire à la doc LTX | Inefficace dans nos essais : masquer au montage | aucun | Astuce propre à Veo |
| Plusieurs plans minutés dans un même prompt | [Veo](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1), [Kling](https://kling.ai/quickstart/klingai-video-3-model-user-guide), [Wan](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt) | LTX-2.5 seulement, doc tierce | Non documenté | Complique le recalage de chaque réplique | **Oui, en pratique** |
| Étiquettes de locuteur `[Personnage, voix]` | [fal](https://blog.fal.ai/kling-3-0-prompting-guide) | Inutile avec un locuteur par plan | Inutile | aucun | Utile seulement à deux locuteurs ou plus |
| Images de référence nommées | Veo, Kling, Grok, Seedance | Image clé → vidéo ; LTX-2.5 Ingredients sur GPU | Image clé → vidéo, « décor + une identité » | aucun | Oui pour les références multiples |
| Voix liée au personnage | Kling, Grok, Wan, Seedance, MiniMax | Non | Non | **Remplacée par nos clones** | Oui |
| LoRA par personnage | [Hugging Face LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3) | Oui, sur GPU loué | Non | aucun | Non |
| Description de timbre détaillée | [UlazAI](https://ulazai.com/character-consistency/) | Peu utile | Peu utile (« deep » jamais obtenu) | **Inutile** : la consigne de voix ne sert qu'à l'énergie du jeu | Non |

Ce tri appelle cinq retouches concrètes de notre fabrique de prompts (`outils/produire.py`), à vérifier par essai. La fonction `ltx_prompt` place aujourd'hui le style en dernier, alors que LTX veut le style nommé tôt. Ce style parle en outre de « movie still », une image fixe, ce qui peut freiner le mouvement dans un prompt vidéo ; c'est une déduction, à tester en remplaçant le mot par « film ». Elle place « No music, no subtitles » au milieu, alors que LTX-2.3 veut la consigne sonore en fin de prompt. Elle cite la réplique d'un bloc, alors que LTX-2.3 conseille de la couper en segments. La consigne Agnes demande même une réplique « in one breath, without pauses », l'inverse de la segmentation, ce qui ne se justifie que si le recalage sur nos voix l'exige. Reste un piège dans la liste négative officielle de LTX : elle se termine par « transition, static » ([Hugging Face LTX-2](https://huggingface.co/Lightricks/LTX-2)). Le mot « static » vise sans doute l'absence de mouvement, mais il entre en conflit avec notre caméra fixe ; mieux vaut ne pas le recopier.

## Conclusion

Le maxi-prompt n'est pas un paragraphe magique, c'est un système de fabrication. Le « maxi » vit dans la bible, la liste de plans et les verrous de continuité ; le prompt envoyé au moteur gratuit ne fait que 120 à 180 mots, dont les trois quarts sont des blocs recopiés à l'identique. La conséquence est pratique. **Ces blocs fixes doivent être assemblés par le code, pas réécrits par un modèle de langage**, car la moindre reformulation (« wearing glasses ») change le personnage. Le modèle de langage n'écrit que la partie variable : le cadrage, le geste, la réplique coupée en segments. Il apparaît aussi que la grammaire des histoires françaises qui marchent en 2026 (une réplique toutes les 2,5 secondes, un locuteur à la fois, des gros plans d'émotion) est précisément celle que nos outils gratuits savent faire : la limite de l'outil devient la forme de la série. Le multi-plans de 15 secondes des modèles payants est séduisant, mais il gênerait le recalage de nos voix clonées, qui sont notre vrai avantage.

L'avantage ne viendra pas d'un secret de prompt, puisque les packs payants revendent des gabarits que tout le monde peut reconstituer gratuitement. Il viendra de l'écriture (réplique choc à 0 seconde, enjeu chiffré, méchant clair, coupure nette, fruit qui porte le rebondissement) et d'une identité qui ne bouge pas d'un épisode à l'autre, voix comprise. Trois incertitudes restent ouvertes et se règlent par des essais, non par la lecture. Aucun éditeur ne garantit le français de LTX. Aucun test contrôlé ne compare les longueurs de prompt, les guillemets ou le JSON. Et rien n'est documenté sur ce que le public veut voir depuis le printemps, sauf ce que mesurent nos propres échantillons.

## Boîte à outils « Rue des Fruits » : deux gabarits à remplir

> **Synthèse Orbeo, pas un fait sourcé.** Les deux gabarits ci-dessous combinent les règles citées dans ce rapport (LTX, Sora, Kling/fal, Aicut, AI Fruit Video, drama-skills, qwe.edu.pl), nos essais du 8 octobre et notre formule interne. Ils n'ont pas été testés tels quels. Ils sont écrits pour LTX-2.x sur Hugging Face, avec Agnes 2.5-flash en secours et nos voix clonées ajoutées ensuite ; les variantes réservées aux modèles payants sont signalées.

### Gabarit 1 · Le maxi-prompt d'un plan

La fiche de plan est notre format de travail : elle n'est jamais envoyée telle quelle au modèle. Les quatre blocs fixes sont recopiés à l'identique depuis `episode.json` (`style`, `persos`, `decors`, `voix`) ; seul le bloc variable change d'un plan à l'autre.

```text
═══ FICHE DE PLAN · RUE DES FRUITS ═══   (format interne, jamais envoyé tel quel)

── BLOC FIXE · STYLE ── identique pour toute la série (episode.json → "style")
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting,
rich detailed set, saturated colors, very expressive faces, vertical 9:16 frame.
(version vidéo, figée elle aussi : « movie still » devient « film », car une « still » est une image fixe)

── BLOC FIXE · PERSONNAGE ── un par personnage visible, copié mot pour mot (30 à 60 mots), jamais le prénom seul
[espèce + couleur et texture de peau] + [visage : yeux, sourcils, bouche] + [cheveux + détail du fruit]
+ [silhouette] + [tenue du jour, ou "the same woman/man, same face… now wearing…"] + [ACCESSOIRE SIGNATURE]
ex. Mamie Prune : a small old grandmother with deep purple wrinkled skin, white hair, small round
glasses, a knitted hat, a knitted beige shawl and a floral dress

── BLOC FIXE · DÉCOR ── un par lieu (episode.json → "decors"), réduit à 2 ou 3 repères dans le prompt
[lieu + moment] + [3 à 5 objets repères] + [lumière : source chaude / source froide] + [3 à 5 couleurs]
+ [ambiance sonore du lieu]
ex. cuisine : small warm old-fashioned grandmother's kitchen at night, floral wallpaper, copper pans,
checkered tablecloth, rain on the window ; son : kitchen room tone, distant rain

── BLOC FIXE · VOIX (jeu seulement) ── règle l'énergie et la bouche ; le timbre réel vient du clone
[âge + genre] + [une texture] + [une énergie] + "speaks in French"
ex. a crackly old woman's voice, warm and mischievous

── BLOC VARIABLE · LE PLAN ──
Durée ............ 3 à 5 s (parole ≤ 4 s) ; nombre d'images = 8n+1, côtés multiples de 32 (LTX)
Cadrage .......... gros plan | plan rapproché taille | plan moyen ; un seul personnage visible
Caméra ........... "locked-off static camera; the framing never changes" (ou UN mouvement lent, jamais pendant la parole)
Geste avant ...... une action visible, au présent ("She pours the tea calmly…")
Réplique ......... ≤ 12 mots, français oral ; coupée à la ponctuation : "segment 1" → [indication de jeu] → "segment 2"
Fin de plan ...... ce que montre la dernière image (raccord avec le plan suivant)
Son .............. ambiance du lieu + un bruit lié au geste + "no music"
Incrustations .... SMS, montants, publications : ajoutés au montage, JAMAIS dans le prompt

── CHAMP NÉGATIF ── noms nus, sans "no" ; ne pas recopier "static" de la liste officielle LTX
```

Rendue en prompt, la fiche devient un seul paragraphe au présent, avec le style en tête et le son en fin. Voici le plan 13 de l'épisode 1, rempli (environ 165 mots).

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting,
saturated colors, vertical 9:16 frame. Medium shot on a locked-off static camera; the framing never
changes. In a small warm old-fashioned grandmother's kitchen at night, with floral wallpaper, hanging
copper pans, a teapot on a checkered tablecloth and rain on the window, a small old grandmother with deep
purple wrinkled skin, white hair, small round glasses, a knitted hat, a knitted beige shawl and a floral
dress stands alone at the stove and calmly pours tea into a cup. She looks up at the camera over her
glasses and speaks in French, in a crackly, warm, mischievous old woman's voice, "Un citron, ma chérie..."
She pauses and raises one eyebrow, then finishes with a sly smile, "Ça finit toujours pressé." Only she
speaks, her lips moving in sync with every word, and the camera holds the frame during the pause.
Audio: small kitchen room tone, soft rain on the window, the clink of the teacup, no music.
```

Le champ négatif reprend notre liste actuelle, complétée par les termes de LTX et de snubroot.

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character,
extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face,
distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality
```

Quand le plan est animé directement sur notre fichier de voix (LTX-2 TURBO, mode « audio-driven »), on retire la réplique du texte. La voix fournie dicte alors les mots et le rythme, et le prompt ne garde que le jeu.

```text
[… même début, jusqu'à « pours tea into a cup. »] She looks up at the camera over her glasses and speaks in
French in a warm, mischievous way; her lips move in sync with the provided voice, and in the short pause she
raises one eyebrow before a sly smile. Only she speaks. The camera holds the frame.
Audio: small kitchen room tone, soft rain on the window, no music.
```

Pour un plan muet de réaction (0,5 à 3 s), on remplace la parole par « No one speaks. » et un geste unique, par exemple « His smile slowly drops into panic, he swallows hard. No one speaks. Party crowd murmur, no music. »

**Variante réservée aux modèles payants** (Kling 3.0, Seedance 2.0, Grok 1.5, Veo 3.1). Elle produit trois plans minutés en une génération de 15 secondes. Kling 3.0 traduit le français en anglais d'après son guide officiel et Seedance 1.5 n'a pas de français ; on ne l'utiliserait donc qu'avec la voix remplacée ou pour des plans muets.

```text
15-second vertical 9:16 fruit melodrama. Stylized semi-realistic 3D CGI animated film, cinematic night
lighting, saturated colors. Three shots joined by hard cuts, no cross-dissolve, no fade.
Shot 1 [0–5 s]: Medium close-up in a small cozy Paris apartment at night, warm lamp and cool blue window
light. [BLOC CERISE]. She holds her smartphone up toward the camera, eyes wet.
[Cherry woman, trembling hurt voice, in French]: "Pourquoi Pêche t'écrit : tu m'as manqué cette nuit ?!"
Shot 2 [5–10 s]: Hard cut. Close-up of [BLOC CITRON] on the grey sofa. He rolls his eyes and leans back.
Immediately, [Lemon man, calm arrogant deep voice, in French]: "Calme-toi… C'est rien, c'est pour le boulot."
Shot 3 [10–15 s]: Hard cut. Extreme close-up of the cherry woman's face; her lips tremble; she does not speak.
Sound: quiet apartment room tone at night, distant traffic, no music.
Continuity: same apartment and same outfits in all shots; only these two characters appear; nothing
appears, disappears or changes shape. Only the active speaker's mouth moves. No subtitles, no on-screen text.
```

Les règles de remplissage tiennent en douze lignes.

| Règle | Pourquoi | Appui |
|---|---|---|
| Style en tête, son en fin | LTX veut le style tôt et la consigne sonore en dernier | [LTX](https://ltx.io/blog/prompting-guide-for-ltx-2), [LTX-2.3](https://ltx.io/blog/directing-dialogue-and-acting) |
| Bloc personnage recopié par le code, jamais reformulé | un mot ajouté change l'identité | [Dinsmore](https://alejandrodinsmore.substack.com/p/deep-dive-veo-3-i-spent-400-testing), [UlazAI](https://ulazai.com/character-consistency/) |
| Aucun prénom seul dans le prompt | sans référence enregistrée, le nom n'est relié à rien ; inversion croissant-baguette dans nos essais | [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos) |
| Un accessoire signature, toujours le même | ancre visuelle contre la dérive | [Flashloop](https://www.flashloop.app/blog/how-to-make-ai-fruit-drama-videos), [drama-skills](https://github.com/zenstory-ai/drama-skills/blob/main/README_EN.md) |
| Un personnage visible, un locuteur | attribution des lèvres ; recomposition des plans larges dans nos essais | [Magic Hour](https://magichour.ai/blog/how-to-prompt-for-speaking-in-veo-3), [OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) |
| Réplique de 12 mots au plus, 4 s au plus | 4 s ≈ une ou deux répliques courtes ; nos voix parlent à environ 2,7 mots/s | [OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) |
| Réplique coupée aux ponctuations, une indication de jeu entre deux | sinon « the timing collapses » | [LTX-2.3](https://ltx.io/blog/directing-dialogue-and-acting) |
| Le geste avant la parole | lie la réplique au bon personnage | [fal](https://blog.fal.ai/kling-3-0-prompting-guide) |
| Une seule consigne de caméra, maintenue pendant les pauses | pas de panoramique pendant le dialogue | [LTX-2.3](https://ltx.io/blog/directing-dialogue-and-acting), [OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) |
| 120 à 180 mots, 4 à 8 phrases | assez de repères, sous les 200 mots | [GitHub LTX-2](https://github.com/Lightricks/LTX-2), [LTX](https://ltx.io/blog/prompting-guide-for-ltx-2) |
| Interdits en noms nus dans le champ négatif, plus une phrase positive dans le texte | les tournures « no X » marchent mal | [Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide) |
| Tout texte à l'écran ajouté au montage | le modèle écrit du charabia (ardoise, faux sous-titres) | nos essais ; [OpenAI](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) (« Avoid signage ») |

### Gabarit 2 · De l'histoire à la liste de plans, par un modèle de langage

Ce gabarit reprend la logique en deux étapes d'Aicut ([aicut.pages.dev](https://aicut.pages.dev/)) : d'abord l'histoire et la liste de plans, puis les prompts, seulement après validation. Il adopte aussi le principe « un battement = un plan = une génération » ([qwe.edu.pl](https://www.qwe.edu.pl/tutorial/short-dramas-ai-beginners-guide/)) et les verrous de drama-skills ([drama-skills](https://github.com/zenstory-ai/drama-skills/blob/main/README_EN.md)). Une différence importante le sépare de ses modèles : **le modèle de langage n'écrit jamais les blocs fixes**. Il produit une liste de plans au format de notre `episode.json`, et le code (`produire.py`) assemble chaque prompt. L'étape 2 sert à relire les prompts, pas à les fabriquer.

```text
Tu es le showrunner, le scénariste et le chef opérateur de « Rue des Fruits », un mélodrame vertical
en français pour TikTok, Reels et Shorts. Le travail se fait en DEUX ÉTAPES. Ne passe jamais à
l'étape 2 sans mon feu vert.

══ CE QUE JE TE DONNE ══
1. LA BIBLE — ne la modifie jamais, ne reformule aucun bloc :
   STYLE : [coller episode.json → "style"]
   PERSONNAGES : pour chacun, identifiant, bloc d'apparence en anglais (copié), tenues disponibles,
   caractère, consigne de voix.
     cerise · citron · peche · kiwi · prune   (réserve : figue, ananas, banane)
   DÉCORS : identifiant, bloc en anglais, ambiance sonore.
   LIMITES : aucune arme, aucune violence physique, aucune nudité ni pose explicite, aucune marque
   ni personne réelle, aucun mineur ; trahison et revanche oui, humiliation gratuite non.
2. L'HISTOIRE DE L'ÉPISODE : [3 à 10 lignes] ou « invente à partir du moteur : [tromperie |
   riche déguisé | revanche de l'humiliée | père indigne | danger caché] ».
3. LA FIN DE L'ÉPISODE PRÉCÉDENT : [dernière réplique + cliffhanger], ou « premier épisode ».
4. LES 5 DERNIERS ÉPISODES : [titre + moteur + chute], pour ne pas répéter la même situation.

══ ÉTAPE 1 · HISTOIRE ET LISTE DE PLANS ══
Rends, dans cet ordre :

A. STRATÉGIE (6 lignes) : moteur ; méchant clair ; victime à qui l'on s'attache ; enjeu chiffré
   (une somme, un délai, un nombre) ; rebondissement ; cliffhanger final. Dis en une ligne ce qui
   change par rapport aux 5 derniers épisodes.

B. BATTEMENTS MINUTÉS, pour 72 à 80 secondes au total :
   0–2 s    le conflit est DÉJÀ en cours : réplique choc, jamais d'introduction ni de générique
            (si c'est une suite, le cliffhanger précédent se résout dans les 10 premières secondes) ;
   2–10 s   le rapport de force et l'enjeu chiffré ;
   10–25 s  première escalade ;
   25–35 s  premier rebondissement (une révélation partielle) ;
   35–60 s  une escalade toutes les 10 secondes environ ;
   60–72 s  renversement ou pic de tension ;
   fin      coupure nette en plein suspense, puis « PARTIE [N+1] ».
   Si possible, que l'espèce d'un fruit porte un indice ou une chute (un jeu de mots, une ressemblance).

C. LISTE DE PLANS, en JSON : un tableau de 22 à 30 objets, chacun au format
   {"id", "decor", "persos": [UN identifiant de personnage ou de tenue],
    "cadre": anglais — taille de plan + position + geste visible, sans prénom,
    "parle": identifiant ou null,
    "jeu": anglais — geste AVANT la parole + verbe de parole (ex. "She pours the tea calmly, looks
           over her glasses and says"), sans prénom,
    "replique": français oral naturel, 12 mots au plus, 4 secondes au plus,
    "segments": la réplique coupée à la ponctuation, avec entre deux segments UNE courte indication
                de jeu en anglais (ex. ["Un citron, ma chérie…", "She raises one eyebrow",
                "Ça finit toujours pressé."]),
    "camera": "locked-off" ou un seul mouvement lent hors parole,
    "duree": secondes estimées,
    "fin_de_plan": anglais — ce que montre la dernière image,
    "musique": "tension" | "triste" | "revanche" | "fete" | null,
    "incrust": texte affiché au montage (SMS, publication, montant) ou null}
   Règles :
   - un seul personnage visible ET un seul locuteur par plan (champ / contre-champ) ;
   - en moyenne une réplique toutes les 2,5 secondes ; 2 à 4 plans muets de réaction de 0,5 à 3 s ;
   - répliques courtes, nettes, émotionnellement claires, compréhensibles sans contexte ;
     si le silence est plus fort, le plan reste muet ;
   - au moins une réplique « citable » de Mamie Prune par épisode ;
   - aucun texte, écran lisible, enseigne ou logo dans l'image : tout texte passe par "incrust" ;
   - le plan qui porte le cliffhanger est désigné dans la stratégie.

D. ACCROCHE (6 mots au plus, en majuscules) et LÉGENDE (l'enjeu ou une question au spectateur,
   puis 3 à 5 hashtags).

E. AUTO-CONTRÔLE : liste chaque plan qui enfreint une règle (deux personnages, réplique trop longue,
   prénom dans "cadre" ou "jeu", texte dans l'image, total hors de 72 à 80 s) et corrige-le.

Puis arrête-toi et attends.

══ ÉTAPE 2 · RELECTURE DES PROMPTS (seulement quand j'écris « étape 2 ») ══
Pour chaque plan, montre le prompt tel que le code l'assemblera : un seul paragraphe en anglais, au
présent, de 120 à 180 mots, dans cet ordre exact, en COPIANT les blocs de la bible sans les changer :
1. STYLE ; 2. cadrage + caméra ("locked-off static camera; the framing never changes") ;
3. DÉCOR réduit à 2 ou 3 repères ; 4. bloc PERSONNAGE complet ; 5. geste avant la parole ;
6. "speaks in French, in [consigne de voix]," puis les segments entre guillemets, séparés par leur
   indication de jeu ; 7. "Only she/he speaks, her/his lips moving in sync with every word, and the
   camera holds the frame during the pauses." ; 8. "Audio: [ambiance du décor], [un bruit lié au
   geste], no music."
Plan muet : remplace 6 et 7 par un geste unique et "No one speaks."
Signale tout prompt de plus de 200 mots et toute phrase qui contredit l'image clé.
Ne change ni l'histoire, ni les personnages, ni les tenues, ni l'ordre des plans.
```

Un plan de sortie attendu, prêt à coller dans `episode.json` :

```json
{"id": 13, "decor": "cuisine", "persos": ["prune"],
 "cadre": "Medium shot, she stands at the stove pouring tea into a cup, looking at the viewer over her glasses with a wise mischievous look.",
 "parle": "prune",
 "jeu": "She pours the tea calmly, looks over her glasses and says with a mischievous smile",
 "replique": "Un citron, ma chérie… Ça finit toujours pressé.",
 "segments": ["Un citron, ma chérie…", "She pauses and raises one eyebrow", "Ça finit toujours pressé."],
 "camera": "locked-off", "duree": 4.0,
 "fin_de_plan": "She holds the teacup, a sly smile, looking straight at the viewer.",
 "musique": "triste", "incrust": null}
```

La relecture humaine se concentre là où le modèle de langage se trompe le plus : la drôlerie des répliques, la vraisemblance des escalades et le respect des limites, soit environ 10 à 15 minutes par épisode. Trois essais vaudraient la peine d'être menés sur une dizaine de plans avant de figer le gabarit. Le premier compare le style en tête et le style en fin de prompt. Le deuxième compare la réplique segmentée et la réplique « d'un souffle », avec mesure du recalage sur nos voix. Le troisième compare une mise en scène en anglais et une mise en scène en français, avec le taux d'erreur whisper et le juge visuel comme seuls arbitres.
