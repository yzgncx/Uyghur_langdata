import sys, csv, operator
import arabic_to_latin

pluralSuff_Arabic = ['لار', 'لەر' ]

pluralSuff_ASCII = ['lar', 'lAr']

pluralSuff_Latin = [ 'lar', 'ler']

possessiveSuff_Arabic = [    'م',    #1sg open-syl                   m
                            'ىم',   # 1sg closed-syl -rnd          im
                            'ۇم',   # 1sg closed-syl +rnd +bck      um
                            'ۈم',   # 1sg closed-syl +rnd -bck      üm
                            'مىز',  # 1pl open-syl                  miz
                            'ىمىز', # 1pl closed-syl                imiz
                            'ڭ',    # 2sg ord open-syl              ng
                            'ىڭ',   # 2sg ord closed-syl -rnd       ing
                            'ۇڭ',   # 2sg ord closed-syl +rnd +bck  ung
                            'ۇڭ',   # 2sg ord closed-syl +rnd -bck  üng
                            'ڭىز',  # 2sg ref open-syl              ngiz
                            'ىڭىز', # 2sg ref closed-syl            ingiz
                            'ڭلار',  # 2pl ord open-syl             nglar
                            'ىڭلار', # 2pl ord closed-syl -rnd      inglar
                            'ۇڭلار',  # 2pl ord closed-syl +rnd +bck   unglar
                            'ۈڭلار',  # 2pl ord closed-syl +rnd -bck   ünglar
                            'ڭىزلار', # 2pl ref open-syl +bck          ngizlar
                            'ڭىزلەر', # 2pl ref open-syl -bck          ngizler
                            'ىڭىزلار', # 2pl ref closed-syl +bck       ingizlar
                            'ىڭىزلەر', # 2pl ref closed-syl -bck       ingizler
                            'لىرى', #2nd person respectful             liri
                            'سى',   #3rd person open-syl               si
                            'ى',     #3rd person closed-syl              i
                    ]

possessiveSuff_ASCII = ['m', 'im', 'um', 'ym', 'miz', 'imiz', 'N', 'iN', 'uN', 'uN', 'Niz', 'iNiz', 'Nlar', 'iNlar', 'uNlar', 'yNlar', 'Nizlar', 'NizlAr', 'iNizlar', 'iNizlAr', 'liri', 'si', 'i']

possessiveSuff_Latin = [    'm',    #1sg open-syl                   m
                            'im',   # 1sg closed-syl -rnd          im
                            'um',   # 1sg closed-syl +rnd +bck      um
                            'üm',   # 1sg closed-syl +rnd -bck      üm
                            'miz',  # 1pl open-syl                  miz
                            'imiz', # 1pl closed-syl                imiz
                            'ng',    # 2sg ord open-syl              ng
                            'ing',   # 2sg ord closed-syl -rnd       ing
                            'ung',   # 2sg ord closed-syl +rnd +bck  ung
                            'üng',   # 2sg ord closed-syl +rnd -bck  üng
                            'ngiz',  # 2sg ref open-syl              ngiz
                            'ingiz', # 2sg ref closed-syl            ingiz
                            'nglar',  # 2pl ord open-syl             nglar
                            'inglar', # 2pl ord closed-syl -rnd      inglar
                            'unglar',  # 2pl ord closed-syl +rnd +bck   unglar
                            'ünglar',  # 2pl ord closed-syl +rnd -bck   ünglar
                            'ngizlar', # 2pl ref open-syl +bck          ngizlar
                            'ngizler', # 2pl ref open-syl -bck          ngizler
                            'ingizlar', # 2pl ref closed-syl +bck       ingizlar
                            'ingizler', # 2pl ref closed-syl -bck       ingizler
                            'liri', #2nd person respectful             liri
                            'si',  #3rd person open-syl               si
                            'i',     #3rd person closed-syl              i
                    ]





personalSuff_Arabic = [  'مەن', # men 1st sg
                        'مىز', # miz 1st pl
                        'سەن', # sen 2nd sg ordinary
                        'سىلەر', # siler 2nd pl ordinary
                        'سىز', # siz 2nd pl ordinary
                        'سىزلەر', # sizler 2nd pl refined
                        'دۇر', # dur 3rd person rg / pl
                    ]

personalSuff_ASCII = ['mAn', 'miz', 'sAn', 'silAr', 'siz', 'sizlAr', 'dur']

personalSuff_Latin = [  'men' # men 1st sg
                        'miz', # miz 1st pl
                        'sen', # sen 2nd sg ordinary
                        'siler', # siler 2nd pl ordinary
                        'siz', # siz 2nd pl ordinary
                        'sizler', # sizler 2nd pl refined
                        'dur', # dur 3rd person rg / pl
                    ]

caseSuff_Arabic = [ 'نىڭ',   #genitive ning
                    'نى', #accusative ni
                    'غا', 'گە', 'قا', 'كە', 'قە', #dative gha ge qa ke qe
                    'دا', 'دە', 'تا', 'تە', #locative da de ta te
                    'دىن', 'تىن', #ablative din tin
                    'دىكى', 'تىكى', #locative qualitative diki tiki
                    '-غىچە', 'گىچە', 'قىچە', 'كىچە', #limitative ghiche giche qiche kiche
                    'دەك', 'تەك', #similitude dek tek
                    'چىلىك', 'چە', #equivalence chilik che
                    'نىڭكى', #representative ningki
                    ]
caseSuff_ASCII = ['niN', 'ni', 'Ga', 'gA', 'qa', 'kA', 'qA', 'da', 'dA', 'ta', 'tA', 'din', 'tin', 'diki', 'tiki', '-GiCA', 'giCA', 'qiCA', 'kiCA', 'dAk', 'tAk', 'Cilik', 'CA', 'niNki']

caseSuff_Latin = [ 'ning',   #genitive ning
                    'ni', #accusative ni
                    'gha','ge','qa','ke','qe', #dative gha ge qa ke qe
                    'da', 'de', 'ta', 'te', #locative da de ta te
                    'din', 'tin', #ablative din tin
                    'diki', 'tiki', #locative qualitative diki tiki
                    'ghiche', 'giche', 'qiche', 'kiche', #limitative ghiche giche qiche kiche
                    'dek', 'tek', #similitude dek tek
                    'chilik', 'che', #equivalence chilik che
                    'ningki', #representative ningki
                    ]

degreeSuff_Arabic = [   'راق', #decreasing degree +back vowel         raq
                        'رەك', #decreasing degree -back vowel       rek
                        'پ', #emphatic degree                       p
                        'غىنا', #endearing degree +voiced +back     ghina
                        'قىنا', #endearing degree -voiced +back     qina
                        'گىنە', #endearing degree +voiced -back     gine
                        'كىنە', #endearing degree -voiced -back     kine
                    ]
degreeSuff_ASCII = ['raq', 'rAk', 'p', 'Gina', 'qina', 'ginA', 'kinA']

degreeSuff_Latin = [   'raq', #decreasing degree +back vowel         raq
                        'rek', #decreasing degree -back vowel       rek
                        'p', #emphatic degree                       p
                        'ghina', #endearing degree +voiced +back     ghina
                        'qina', #endearing degree -voiced +back     qina
                        'gine', #endearing degree +voiced -back     gine
                        'kine', #endearing degree -voiced -back     kine
                    ]


verbalSuff_Latin = ['iwatqanidinglar', 'maywatqanidimmu', 'maywatiptimenmu',
                    'mighanidinglar', 'iwatattingllar', 'iwatqanidingiz',
                    'maydighanmenmu', 'mighanmusiler', 'ghanmidinglar',
                    'mighanidingiz', 'mighanidingmu', 'iwatqanidilar',
                    'iwatqanidimmu', 'maywatqanidim', 'maywatiptimen',
                    'ghanidinglar', 'ghanmidingiz', 'mighanidimmu', 'maywatisiler',
                    'maywatimenmu', 'iwatattingiz', 'iwatqaniding', 'idighansiler',
                    'maydighanmen', 'meydighanmen', 'maqqimusiler', 'watiptimenmu',
                    'iptikensiler', 'midinglarmu', 'ghanmusiler', 'mighansiler',
                    'mighanmenmu', 'mighanmusen', 'mighanmizmu', 'mighanmusiz',
                    'ghanidingiz', 'mighaniding', 'maywatattim', 'iwatmayttim',
                    'iwatqanidim', 'iwatqaniduq', 'ettim yttim', 'mayttinglar',
                    'idighanmenu', 'iwatsanglar', 'malar meler', 'maymu meymu',
                    'midingizmu', 'ghanmiding', 'mighanidim', 'mighaniduq',
                    'iwatisiler', 'iwatimenmu', 'maywatimen', 'maywatisen',
                    'maywatimiz', 'maywatisiz', 'iwatatting', 'iwatmamtim',
                    'iwatqanidi', 'mayttingiz', 'idighanmen', 'idighansen',
                    'idighanmiz', 'idighansiz', 'iwetsingiz', 'almaymenmu',
                    'maqqisiler', 'maqqimenmu', 'maqqimusen', 'maqqimizmu',
                    'maqqimusiz', 'maqtisiler', 'maqtimenmu', 'maptimenmu',
                    'watiptimen', 'watiptimiz', 'watipsiler', 'iptikenmen',
                    'iptikensen', 'iptikenmiz', 'iptikensiz', 'dinglarmu', 'midinglar',
                    'ghansiler', 'ghanmanmu', 'ghanmusan', 'ghanmizmu', 'ghanmusiz',
                    'mighanmen', 'mighansen', 'mighanmiz', 'mighansiz', 'ghaniding',
                    'ghanmidim', 'ghanmiduq', 'mighanidi', 'mighanidi', 'maywatidu',
                    'maywatidu', 'iwatattim', 'iwatattuq', 'iwatamtim', 'attinglar',
                    'mayttimmu', 'misanglar', 'maywatsam', 'mang meng', 'alaysiler',
                    'alaymenmu', 'aliyamsen', 'iptimenmu', 'maysiler', 'maymenmu',
                    'maymizmu', 'mamsiler', 'dingizmu', 'midingiz', 'midingmu',
                    'mighanmu', 'mighanmu', 'ghanidim', 'ghaniduq', 'ghanmidi',
                    'ghanmidi', 'iwatimen', 'iwatisen', 'iwatimiz', 'iwatisiz', 
                    'iwatatti', 'iwatatti', 'masmenmu', 'attingiz', 'attingmu',
                    'maytting', 'misingiz', 'iwatsang', 'misingiz', 'aliyamdu',
                    'almaymen', 'maqqimen', 'maqqisen', 'maqqimiz', 'maqqisiz',
                    'maqtimen', 'maqtisen', 'maqtimiz', 'maqtisiz', 'maptimen',
                    'meptimen', 'maptimiz', 'mapsiler', 'mapsenmu', 'watipsen',
                    'watipsiz', 'amsiler', 'maymudi', 'dinglar', 'midimmu', 'miduqmu',
                    'ghanmen', 'ghansen', 'ghanmiz', 'ghansiz', 'ghantim', 'ghanidi',
                    'ghanidi', 'iwatidu', 'iwatidu', 'arsiler', 'armanmu', 'armusan',
                    'attimmu', 'mayttim', 'meyttim', 'mayttuq', 'idighan', 'idighan',
                    'idighan', 'idighan', 'idighan', 'idighan', 'idighan', 'idighan',
                    'idighan', 'idighan', 'idighan', 'idighan', 'sanglar', 'senglar',
                    'iwatsam', 'iwatsaq', 'misalar', 'misunmu', 'alaymen', 'alaysen',
                    'alaymiz', 'alaysiz', 'maqqimu', 'maqqimu', 'iptimen', 'iptimiz',
                    'ipsiler', 'ipsenmu', 'maptumu', 'watiptu', 'watiptu', 'iptiken',
                    'iptiken', 'masliq', 'mesliq', 'isiler', 'imenmu', 'maymen', 'meymen',
                    'maysen', 'maymiz', 'maysiz', 'mamsen', 'mamsem', 'mamsiz', 'dingiz',
                    'dingmu', 'miding', 'midimu', 'midimu', 'ghanmu', 'ghanmu', 'mighan',
                    'mighan', 'masmen', 'massen', 'atting', 'attimu', 'maytti', 'maytti',
                    'singiz', 'misang', 'iwatsa', 'iwatsa', 'singiz', 'misang', 'inglar',
                    'mighin', 'alaydu', 'alaydu', 'iptumu', 'mapsen', 'mapsiz', 'amsen',
                    'ammiz', 'amsiz', 'maydu', 'maydu', 'maydu', 'dimmu', 'emduq', 'midim',
                    'miduq', 'arman', 'arsan', 'armiz', 'arsiz', 'attim', 'attuq', 'misam',
                    'misem', 'misaq', 'misek', 'salar', 'misam', 'misaq', 'nglar', 'misun',
                    'mayli', 'meyli', 'misun', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi',
                    'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi',
                    'maqta', 'mekte', 'maqta', 'ipsen', 'ipsiz', 'maptu', 'maptu', 'imen',
                    'ymen', 'isen', 'imiz', 'isiz', 'amdu', 'amdu', 'ding', 'emdi', 'dimu',
                    'emdi', 'midi', 'midi', 'ghan', 'ghan', 'armu', 'atti', 'atti', 'sang',
                    'seng', 'misa', 'misa', 'sang', 'misa', 'ayli', 'eyli', 'aymu', 'eymu',
                    'eley', 'elme', 'iptu', 'iptu', 'maq', 'mek', 'idu', 'idu', 'dim', 'dum',
                    'düm', 'duq', 'mey', 'mey', 'mey', 'mas', 'sam', 'sem', 'saq', 'sek',
                    'sam', 'saq', 'sun', 'ing', 'ung', 'üng', 'sun', 'may', 'mey', 'mek',
                    'di', 'di', 'ar', 'ar', 'sa', 'se', 'sa', 'sa', 'ay', 'ey', 'ng', 'ma', 'me', 'y'
                    ]

verbalSuff_ASCII = ['iwatqanidiNlar', 'majwatqanidimmu', 'majwatiptimAnmu', 'miGanidiNlar', 'iwatattiNllar', 'iwatqanidiNiz', 'majdiGanmAnmu', 'miGanmusilAr', 'GanmidiNlar', 'miGanidiNiz', 'miGanidiNmu', 'iwatqanidilar', 'iwatqanidimmu', 'majwatqanidim', 'majwatiptimAn', 'GanidiNlar', 'GanmidiNiz', 'miGanidimmu', 'majwatisilAr', 'majwatimAnmu', 'iwatattiNiz', 'iwatqanidiN', 'idiGansilAr', 'majdiGanmAn', 'mAjdiGanmAn', 'maqqimusilAr', 'watiptimAnmu', 'iptikAnsilAr', 'midiNlarmu', 'GanmusilAr', 'miGansilAr', 'miGanmAnmu', 'miGanmusAn', 'miGanmizmu', 'miGanmusiz', 'GanidiNiz', 'miGanidiN', 'majwatattim', 'iwatmajttim', 'iwatqanidim', 'iwatqaniduq', 'Attim jttim', 'majttiNlar', 'idiGanmAnu', 'iwatsaNlar', 'malar mAlAr', 'majmu mAjmu', 'midiNizmu', 'GanmidiN', 'miGanidim', 'miGaniduq', 'iwatisilAr', 'iwatimAnmu', 'majwatimAn', 'majwatisAn', 'majwatimiz', 'majwatisiz', 'iwatattiN', 'iwatmamtim', 'iwatqanidi', 'majttiNiz', 'idiGanmAn', 'idiGansAn', 'idiGanmiz', 'idiGansiz', 'iwAtsiNiz', 'almajmAnmu', 'maqqisilAr', 'maqqimAnmu', 'maqqimusAn', 'maqqimizmu', 'maqqimusiz', 'maqtisilAr', 'maqtimAnmu', 'maptimAnmu', 'watiptimAn', 'watiptimiz', 'watipsilAr', 'iptikAnmAn', 'iptikAnsAn', 'iptikAnmiz', 'iptikAnsiz', 'diNlarmu', 'midiNlar', 'GansilAr', 'Ganmanmu', 'Ganmusan', 'Ganmizmu', 'Ganmusiz', 'miGanmAn', 'miGansAn', 'miGanmiz', 'miGansiz', 'GanidiN', 'Ganmidim', 'Ganmiduq', 'miGanidi', 'miGanidi', 'majwatidu', 'majwatidu', 'iwatattim', 'iwatattuq', 'iwatamtim', 'attiNlar', 'majttimmu', 'misaNlar', 'majwatsam', 'maN mAN', 'alajsilAr', 'alajmAnmu', 'alijamsAn', 'iptimAnmu', 'majsilAr', 'majmAnmu', 'majmizmu', 'mamsilAr', 'diNizmu', 'midiNiz', 'midiNmu', 'miGanmu', 'miGanmu', 'Ganidim', 'Ganiduq', 'Ganmidi', 'Ganmidi', 'iwatimAn', 'iwatisAn', 'iwatimiz', 'iwatisiz', 'iwatatti', 'iwatatti', 'masmAnmu', 'attiNiz', 'attiNmu', 'majttiN', 'misiNiz', 'iwatsaN', 'misiNiz', 'alijamdu', 'almajmAn', 'maqqimAn', 'maqqisAn', 'maqqimiz', 'maqqisiz', 'maqtimAn', 'maqtisAn', 'maqtimiz', 'maqtisiz', 'maptimAn', 'mAptimAn', 'maptimiz', 'mapsilAr', 'mapsAnmu', 'watipsAn', 'watipsiz', 'amsilAr', 'majmudi', 'diNlar', 'midimmu', 'miduqmu', 'GanmAn', 'GansAn', 'Ganmiz', 'Gansiz', 'Gantim', 'Ganidi', 'Ganidi', 'iwatidu', 'iwatidu', 'arsilAr', 'armanmu', 'armusan', 'attimmu', 'majttim', 'mAjttim', 'majttuq', 'idiGan', 'idiGan', 'idiGan', 'idiGan', 'idiGan', 'idiGan', 'idiGan', 'idiGan', 'idiGan', 'idiGan', 'idiGan', 'idiGan', 'saNlar', 'sANlar', 'iwatsam', 'iwatsaq', 'misalar', 'misunmu', 'alajmAn', 'alajsAn', 'alajmiz', 'alajsiz', 'maqqimu', 'maqqimu', 'iptimAn', 'iptimiz', 'ipsilAr', 'ipsAnmu', 'maptumu', 'watiptu', 'watiptu', 'iptikAn', 'iptikAn', 'masliq', 'mAsliq', 'isilAr', 'imAnmu', 'majmAn', 'mAjmAn', 'majsAn', 'majmiz', 'majsiz', 'mamsAn', 'mamsAm', 'mamsiz', 'diNiz', 'diNmu', 'midiN', 'midimu', 'midimu', 'Ganmu', 'Ganmu', 'miGan', 'miGan', 'masmAn', 'massAn', 'attiN', 'attimu', 'majtti', 'majtti', 'siNiz', 'misaN', 'iwatsa', 'iwatsa', 'siNiz', 'misaN', 'iNlar', 'miGin', 'alajdu', 'alajdu', 'iptumu', 'mapsAn', 'mapsiz', 'amsAn', 'ammiz', 'amsiz', 'majdu', 'majdu', 'majdu', 'dimmu', 'Amduq', 'midim', 'miduq', 'arman', 'arsan', 'armiz', 'arsiz', 'attim', 'attuq', 'misam', 'misAm', 'misaq', 'misAk', 'salar', 'misam', 'misaq', 'Nlar', 'misun', 'majli', 'mAjli', 'misun', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqqi', 'maqta', 'mAktA', 'maqta', 'ipsAn', 'ipsiz', 'maptu', 'maptu', 'imAn', 'jmAn', 'isAn', 'imiz', 'isiz', 'amdu', 'amdu', 'diN', 'Amdi', 'dimu', 'Amdi', 'midi', 'midi', 'Gan', 'Gan', 'armu', 'atti', 'atti', 'saN', 'sAN', 'misa', 'misa', 'saN', 'misa', 'ajli', 'Ajli', 'ajmu', 'Ajmu', 'AlAj', 'AlmA', 'iptu', 'iptu', 'maq', 'mAk', 'idu', 'idu', 'dim', 'dum', 'dym', 'duq', 'mAj', 'mAj', 'mAj', 'mas', 'sam', 'sAm', 'saq', 'sAk', 'sam', 'saq', 'sun', 'iN', 'uN', 'yN', 'sun', 'maj', 'mAj', 'mAk', 'di', 'di', 'ar', 'ar', 'sa', 'sA', 'sa', 'sa', 'aj', 'Aj', 'N', 'ma', 'mA', 'j']

verbalSuff_Arabic = ['ىۋاتقانىدىڭلار', 'مايۋاتقانىدىممئۇ', 'مايۋاتىپتىمەنمئۇ', 'مىغانىدىڭلار',
                        'ىۋاتاتتىڭللار', 'ىۋاتقانىدىڭىز', 'مايدىغانمەنمئۇ', 'مىغانمۇسىلەر', 
                        'غانمىدىڭلار', 'مىغانىدىڭىز', 'مىغانىدىڭمئۇ', 'ىۋاتقانىدىلار', 'ىۋاتقانىدىممئۇ',
                        'مايۋاتقانىدىم', 'مايۋاتىپتىمەن', 'غانىدىڭلار', 'غانمىدىڭىز', 'مىغانىدىممئۇ', 
                        'مايۋاتىسىلەر', 'مايۋاتىمەنمئۇ', 'ىۋاتاتتىڭىز', 'ىۋاتقانىدىڭ', 'ىدىغانسىلەر',
                        'مايدىغانمەن', 'مەيدىغانمەن', 'ماققىمۇسىلەر', 'ۋاتىپتىمەنمئۇ',
                        'ىپتىكەنسىلەر', 'مىدىڭلارمئۇ', 'غانمۇسىلەر', 'مىغانسىلەر',
                        'مىغانمەنمئۇ', 'مىغانمۇسەن', 'مىغانمىزمئۇ', 'مىغانمۇسىز', 'غانىدىڭىز', 
                        'مىغانىدىڭ', 'مايۋاتاتتىم', 'ىۋاتمايتتىم', 'ىۋاتقانىدىم', 'ىۋاتقانىدۇق', 
                        'ەتتىم يتتىم', 'مايتتىڭلار', 'ىدىغانمەنئۇ', 'ىۋاتساڭلار', 'مالار مەلەر', 
                        'مايمۇ مەيمئۇ', 'مىدىڭىزمئۇ', 'غانمىدىڭ', 'مىغانىدىم', 'مىغانىدۇق', 'ىۋاتىسىلەر',
                        'ىۋاتىمەنمئۇ', 'مايۋاتىمەن', 'مايۋاتىسەن', 'مايۋاتىمىز', 'مايۋاتىسىز',
                        'ىۋاتاتتىڭ', 'ىۋاتمامتىم', 'ىۋاتقانىدئى', 'مايتتىڭىز', 'ىدىغانمەن',
                        'ىدىغانسەن', 'ىدىغانمىز', 'ىدىغانسىز', 'ىۋەتسىڭىز', 'المايمەنمئۇ', 'ماققىسىلەر',
                        'ماققىمەنمئۇ', 'ماققىمۇسەن', 'ماققىمىزمئۇ', 'ماققىمۇسىز', 'ماقتىسىلەر', 'ماقتىمەنمئۇ',
                        'ماپتىمەنمئۇ', 'ۋاتىپتىمەن', 'ۋاتىپتىمىز', 'ۋاتىپسىلەر', 'ىپتىكەنمەن', 'ىپتىكەنسەن',
                        'ىپتىكەنمىز', 'ىپتىكەنسىز', 'دىڭلارمئۇ', 'مىدىڭلار', 'غانسىلەر', 'غانمانمئۇ', 'غانمۇسان',
                        'غانمىزمئۇ', 'غانمۇسىز', 'مىغانمەن', 'مىغانسەن', 'مىغانمىز', 'مىغانسىز', 'غانىدىڭ', 'غانمىدىم',
                        'غانمىدۇق', 'مىغانىدئى', 'مىغانىدئى', 'مايۋاتىدئۇ', 'مايۋاتىدئۇ', 'ىۋاتاتتىم', 'ىۋاتاتتۇق',
                        'ىۋاتامتىم', 'اتتىڭلار', 'مايتتىممئۇ', 'مىساڭلار', 'مايۋاتسام', 'ماڭ مەڭ', 'الايسىلەر',
                        'الايمەنمئۇ', 'الىيامسەن', 'ىپتىمەنمئۇ', 'مايسىلەر', 'مايمەنمئۇ', 'مايمىزمئۇ', 'مامسىلەر',
                        'دىڭىزمئۇ', 'مىدىڭىز', 'مىدىڭمئۇ', 'مىغانمئۇ', 'مىغانمئۇ', 'غانىدىم', 'غانىدۇق', 'غانمىدئى',
                        'غانمىدئى', 'ىۋاتىمەن', 'ىۋاتىسەن', 'ىۋاتىمىز', 'ىۋاتىسىز', 'ىۋاتاتتئى', 'ىۋاتاتتئى',
                        'ماسمەنمئۇ', 'اتتىڭىز', 'اتتىڭمئۇ', 'مايتتىڭ', 'مىسىڭىز', 'ىۋاتساڭ', 'مىسىڭىز',
                        'الىيامدئۇ', 'المايمەن', 'ماققىمەن', 'ماققىسەن', 'ماققىمىز', 'ماققىسىز', 'ماقتىمەن',
                        'ماقتىسەن', 'ماقتىمىز', 'ماقتىسىز', 'ماپتىمەن', 'مەپتىمەن', 'ماپتىمىز', 'ماپسىلەر',
                        'ماپسەنمئۇ', 'ۋاتىپسەن', 'ۋاتىپسىز', 'امسىلەر', 'مايمۇدئى', 'دىڭلار', 'مىدىممئۇ',
                        'مىدۇقمئۇ', 'غانمەن', 'غانسەن', 'غانمىز', 'غانسىز', 'غانتىم', 'غانىدئى', 'غانىدئى',
                        'ىۋاتىدئۇ', 'ىۋاتىدئۇ', 'ارسىلەر', 'ارمانمئۇ', 'ارمۇسان', 'اتتىممئۇ', 'مايتتىم', 'مەيتتىم',
                        'مايتتۇق', 'ىدىغان', 'ىدىغان', 'ىدىغان', 'ىدىغان', 'ىدىغان', 'ىدىغان', 'ىدىغان', 'ىدىغان',
                        'ىدىغان', 'ىدىغان', 'ىدىغان', 'ىدىغان', 'ساڭلار', 'سەڭلار', 'ىۋاتسام', 'ىۋاتساق', 'مىسالار',
                        'مىسۇنمئۇ', 'الايمەن', 'الايسەن', 'الايمىز', 'الايسىز', 'ماققىمئۇ', 'ماققىمئۇ', 'ىپتىمەن',
                        'ىپتىمىز', 'ىپسىلەر', 'ىپسەنمئۇ', 'ماپتۇمئۇ', 'ۋاتىپتئۇ', 'ۋاتىپتئۇ', 'ىپتىكەن',
                        'ىپتىكەن', 'ماسلىق', 'مەسلىق', 'ىسىلەر', 'ىمەنمئۇ', 'مايمەن', 'مەيمەن', 'مايسەن',
                        'مايمىز', 'مايسىز', 'مامسەن', 'مامسەم', 'مامسىز', 'دىڭىز', 'دىڭمئۇ', 'مىدىڭ', 'مىدىمئۇ',
                        'مىدىمئۇ', 'غانمئۇ', 'غانمئۇ', 'مىغان', 'مىغان', 'ماسمەن', 'ماسسەن', 'اتتىڭ', 'اتتىمئۇ',
                        'مايتتئى', 'مايتتئى', 'سىڭىز', 'مىساڭ', 'ىۋاتسئا', 'ىۋاتسئا', 'سىڭىز', 'مىساڭ',
                        'ىڭلار', 'مىغىن', 'الايدئۇ', 'الايدئۇ', 'ىپتۇمئۇ', 'ماپسەن', 'ماپسىز', 'امسەن', 'اممىز',
                        'امسىز', 'مايدئۇ', 'مايدئۇ', 'مايدئۇ', 'دىممئۇ', 'ەمدۇق', 'مىدىم', 'مىدۇق', 'ارمان', 'ارسان', 
                        'ارمىز', 'ارسىز', 'اتتىم', 'اتتۇق', 'مىسام', 'مىسەم', 'مىساق', 'مىسەك', 'سالار', 'مىسام',
                        'مىساق', 'ڭلار', 'مىسۇن', 'مايلئى', 'مەيلئى', 'مىسۇن', 'ماققئى', 'ماققئى', 'ماققئى',
                        'ماققئى', 'ماققئى', 'ماققئى', 'ماققئى', 'ماققئى', 'ماققئى', 'ماققئى', 'ماققئى', 'ماققئى', 
                        'ماققئى', 'ماقتئا', 'مەكتئە', 'ماقتئا', 'ىپسەن', 'ىپسىز', 'ماپتئۇ', 'ماپتئۇ', 'ىمەن',
                        'يمەن', 'ىسەن', 'ىمىز', 'ىسىز', 'امدئۇ', 'امدئۇ', 'دىڭ', 'ەمدئى', 'دىمئۇ', 'ەمدئى', 'مىدئى',
                        'مىدئى', 'غان', 'غان', 'ارمئۇ', 'اتتئى', 'اتتئى', 'ساڭ', 'سەڭ', 'مىسئا', 'مىسئا', 'ساڭ',
                        'مىسئا', 'ايلئى', 'ەيلئى', 'ايمئۇ', 'ەيمئۇ', 'ەلەي', 'ەلمئە', 'ىپتئۇ', 'ىپتئۇ', 'ماق',
                        'مەك', 'ىدئۇ', 'ىدئۇ', 'دىم', 'دۇم', 'دۈم', 'دۇق', 'مەي', 'مەي', 'مەي', 'ماس', 'سام', 'سەم',
                        'ساق', 'سەك', 'سام', 'ساق', 'سۇن', 'ىڭ', 'ۇڭ', 'ۈڭ', 'سۇن', 'ماي', 'مەي', 'مەك', 'دئى',
                        'دئى', 'ار', 'ار', 'سئا', 'سئە', 'سئا', 'سئا', 'اي', 'ەي', 'ڭ', 'مئا', 'مئە', 'ي'
                        ]





def stripNounSuff(word):
    # at -lar -imiz -Ga
    result = word
    for affix in caseSuff_ASCII:
        if result.endswith(affix):
            result = result[:-(len(affix))]
            break
    for affix in possessiveSuff_ASCII:
        if result.endswith(affix):
            result = result[:-(len(affix))]
            break
    for affix in pluralSuff_ASCII:
        if result.endswith(affix):
            result = result[:-(len(affix))]
            break
    return result

def stripPersonalNounSuff(word):
    result = word
    for affix in caseSuff_ASCII:
        if result.endswith(affix):
            result = result[:-(len(affix))]
            break
    for affix in personalSuff_ASCII:
        if result.endswith(affix):
            result = result[:-(len(affix))]
            break
    for affix in pluralSuff_ASCII:
        if result.endswith(affix):
            result = result[:-(len(affix))]
            break
    return result


def stripAdjSuff(word):
    result = word
    for affix in degreeSuff_ASCII:
        if result.endswith(affix):
            result = result[:-(len(affix))]
            break
    return result

def stripVerbSuff(word):
    result = word
    for affix in verbalSuff_ASCII:
        if result.endswith(affix):
            result = result[:-(len(affix))]
            break
    return result

def main(argv):
# first argument:   corpus
# second argument:  stem dict
# third argument:   outfile

#    ascii_suff = []
#    for suffix in verbalSuff_Arabic:
#        ascii_suff.append(arabic_to_latin.arabic_to_ASCII(suffix))
#    print(ascii_suff)

    stemslist = []
    with open(argv[1]) as stem_dict:
        stem_dict_r = csv.DictReader(stem_dict)
        for row in stem_dict_r:
            stemslist.append(row['entry_ug_ASCII'])
    stems = set(stemslist)

    stripped_header = ['original', 'stripped', 'in_dict', 'monosegmental', 'zero_diff']
    stripped_csv = []
    with open(argv[0]) as corpus:
        dr = csv.DictReader(corpus) 
        for i, row in enumerate(dr):
            original = row['word']
            #limit stems to novel instances for a given inflected word
            tmp = []


            persn_stem = stripPersonalNounSuff(original)
            persn_indict = int(persn_stem in stems)
            persn_monoseg = int(len(persn_stem) == 1)
            tmp.append({'original' : original, 'stripped' : persn_stem,
                        'in_dict' : persn_indict, 'monosegmental' : persn_monoseg, 'zero_diff' : int(persn_stem == original)})

            noun_stem = stripNounSuff(original)
            noun_indict = int(noun_stem in stems)
            noun_monoseg = int(len(noun_stem) == 1)
            #only append it if it's a unique stem based on the 4 stripping methods
            if not list(map(operator.itemgetter('stripped'),tmp)).count(noun_stem):
                tmp.append({'original' : original, 'stripped' : noun_stem,
                             'in_dict' : noun_indict, 'monosegmental' : noun_monoseg, 'zero_diff' : int(noun_stem == original)})

            verb_stem = stripVerbSuff(original)
            verb_indict = int(verb_stem in stems)
            verb_monoseg = int(len(verb_stem) == 1)
            #only append it if it's a unique stem based on the 4 stripping methods
            if not list(map(operator.itemgetter('stripped'),tmp)).count(verb_stem): 
                tmp.append({'original' : original, 'stripped' : verb_stem,
                                 'in_dict' : verb_indict, 'monosegmental' : verb_monoseg, 'zero_diff' : int(verb_stem == original)})

            adj_stem = stripAdjSuff(original)
            adj_indict = int(adj_stem in stems)
            adj_monoseg = int(len(adj_stem) == 1)
            #only append it if it's a unique stem based on the 4 stripping methods
            if not list(map(operator.itemgetter('stripped'),tmp)).count(adj_stem):
                stripped_csv.append({'original' : original, 'stripped' : adj_stem,
                                     'in_dict' : adj_indict, 'monosegmental' : adj_monoseg, 'zero_diff' : int(adj_stem == original)})

            if i % 1000 == 0:
                print("row " + str(i) + " completed.")
            stripped_csv = stripped_csv + tmp


    with open(argv[2], 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, stripped_header)
        writer.writeheader()
        for row in stripped_csv:
             writer.writerow(dict((k, v) for k, v in row.items()))



    print("done :)")
    return 

if __name__ == '__main__':
    main(sys.argv[1:])


