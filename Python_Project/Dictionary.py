while True:
    a = input().lower()
    word = {'my':'আমার','you':'তুমি','i':'আমি','eat':'খাওয়া','a':'একটি','above':'উপরে','accident':'দূর্ঘটনা',
            'add':'সংযুক্ত','love':'ভালোবাসা','what':'কী','leader':'নেতা','famous':'বিখ্যাত','wonderful':'বিস্ময়কর',
            'fill':'ভরাট','consider':' বিবেচনা','lawyer':'আইনজীবী','resigned':'পদত্যাগ','defeated':'পরাজিত',
            'revolution':'বিপ্লব','popular':'জনপ্রিয়','diagnose':'লক্ষণ দেখিয়া নির্ণয় করা','they':'তারা',
            'education':'শিক্ষা','find':'ভালো','advanced':'অগ্রসর','publication':'প্রকাশন','boy':'বালক','girl':'বালিকা',
            'married':'বিবাহিত','book':'বই','proposed':'প্রস্তাবিত','election':' নির্বাচন','historical':'ঐতিহাসিক',
            'gratitude':'কৃতজ্ঞতা','teacher':'শিক্ষক','independent':'স্বাধীন','located':'অবস্থিত','established':'প্রতিষ্ঠিত',
            'institution':'প্রতিষ্ঠান ','program':'কার্যক্রম','active':'সক্রিয়','why':'কেন','your':'তোমার','very':'খুব',
            'city':'শহর','is':'হয়','and':'এবং','in':'মধ্যে','many':'অনেক','life':'জীবন','elected':'নির্বাচিত',
            'gained':'অর্জন','blood':'রক্ত','war':'যুদ্ধ','communication':'যোগাযোগ','caste':'বর্ণ','currency':'মুদ্রা',
            'creed':'ধর্মমত','choose':'নির্বাচন করুন','best':'শ্রেষ্ঠ','miserably':'শোচনীয়ভাবে',
            'true':'সত্য','village':'গ্রাম','after':'পরে','to':'হতে','so':'তাই','go':'যাওয়া','back':'পিছনে',
            'or':'অথবা','try':'আবার','develop':'উন্নতি','pollution':'দূষণ','alternative':'বিকল্প','become':'হই',
            'duration':'স্থিতিকাল','our':'আমাদের','liberation':'মুক্তিযুদ্ধ','freedom':'স্বাধীনতা','country':'দেশ',
            'passage':'উত্তরণ','peak':'শিখর','author':'লেখক','dramatist':'নাট্যকার',
            'want':'প্রয়োজন','for':'জন্য','loop':'ঘুরানো','correct':'সঠিক','answer':'উত্তর','give':'সাহায্য',
            'false':'মিথ্যা','if':'যদি','slow':'ধীরে-ধীরে','the':'টি,টা','that':'যে','with':'সাথে','one':'এক',
            'two':'দুই','tradition':'ঐীতহ্য','hour':'ঘণ্টা','roport':'প্রতিবেদন','no':'না','film':'চলচ্চিত্র',
            'maker':'সৃষ্টিকর্তা','fame':'খ্যাতি','admiration':' শ্রদ্ধা','fiction':'কথাসাহিত্য',
            'wait':'অপেক্ষা','me':'আমাকে','like':'পছন্দ','do':'করা','work':'কাজ','people':'জনগণ','new':'নতুন',
            'today':'আজ','small':'ছোট','was':'ছিল','enough':'যথেষ্ট্য','big':'বড়','but':'কিন্তু','have':'আছে',
            'she':'তিনি','he':'সে','head':'মাথা','time':'সময়','buried':'প্রোথিত','physics':'পদার্থবিদ্যা','early':'তাড়াতাড়ি',
            'age':'বয়স','cosmology':'সৃষ্টিতত্ব','receive':'গ্রহণ','now':'এখন','knowledge':'জ্ঞান','word':'শব্দ','fun':'মজা',
            'write':'লেখা','international':'আন্তর্জাতিক','day':'দিন','language':'ভাষা','form':'আকৃতি','gaps':'ফাঁক',
            'month':'মাস','never':'কখনো না','young':'তরুণ,যুবক','alltime':'সবসময়','question':'প্রশ্ন','her':'তার',
            'read':'পড়া','woman':'মহিলা','fortune':'ভাগ্য','prestigious':'ভোজবাজিপূর্ণ','theoretical':'তাত্ত্বিক',  
            'list':'তালিকা','cost':'খরচ','from':'থেকে','control':'নিয়ন্ত্রণ','manage':'পরিচালনা করা','enter':'প্রবেশ',
            'come':'আসা','practice':'চর্চা করা','heavy':'ভারী','english':'ইংরেজি','mother':'মা','father':'বাবা',
            'until':'পর্যন্ত','first':'প্রথম','year':'বছর','about':'প্রায়','it':'এটা','follow':'লক্ষ করা',
            'mobile':'মুঠোফোন','research':'গবেষণা','sentence':'বাক্য','increase':'বৃদ্ধি','order':'আদেশ',
            'primary':'প্রাথমিক','martyr':'শহীদ','wealthy':' ধনী','planter':'আবাদকারী','inherited':'উত্তরাধিকারসূত্রে',
            'experience':' অভিজ্ঞতা','prime minister':'প্রধানমন্ত্রী','general':'সাধারণ','secretary':'সম্পাদক',
            'rubbish':'আবর্জনা','smoke':'ধোঁয়া','nice':'সুন্দর','beatiful':'সুন্দর','milk':'দুধ','water':'পানি',
            'serious':'গুরুতর','location':'অবস্থান','industrial':'শিল্প','construction':'নির্মাণ','import':'আমদানি',
            'important':'গুরুত্বপূর্ণ','society':'সমাজ','always':'সবসময়','man':'মানুষ','majority':'সংখ্যাগরিষ্ঠ',
            'student':'ছাত্র','men':'পুরুষ','most':'সবচেয়ে','modern':'আধুনিক','any':'কোনো','easy':'সহজ',
            'preposition':'অব্যয়','top':'শীর্ষ','under':'অধীনে','how':'কিভাবে','pose':'অঙ্গবিক্ষেপ','huge':'বিশাল',
            'below':'নিচে','basic':'মৌলিক','need':'প্রয়োজন','illiterate':'অশিক্ষিত','burial':'কবর ',
            'transfer':'হস্তান্তর','information':'তথ্য','instantaneous':'ক্ষণিক','national':'জাতীয়','song':'গান',
            'globalization':'বিশ্বায়ন','relation':'সম্পর্ক','belief':'বিশ্বাস','use':'ব্যবহার','useful':'দরকারী',
            'physical':'শারীরিক','gender':'লিঙ্গ','their':'তাদের','different':'ভিন্ন','worst':'খারাপ',
            'parent':' পিতা বা মাতা','protest':'প্রতিবাদ','topics':'বিষয়','boss':'মনিব','really':'সত্যিই'}
    if a in word:

        print(word[a])
    else:
        print("Sorry!\n",a,"This not found")


               
