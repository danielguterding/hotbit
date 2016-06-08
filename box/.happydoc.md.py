(S'eb620a20b854ca69f2419f6edb7859f3'
p1
(ihappydoclib.parseinfo.moduleinfo
ModuleInfo
p2
(dp3
S'_namespaces'
p4
((dp5
S'Atom'
p6
(ihappydoclib.parseinfo.classinfo
ClassInfo
p7
(dp8
g4
((dp9
(dp10
S'__init__'
p11
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p12
(dp13
g4
((dp14
(dp15
tp16
sS'_exception_info'
p17
(dp18
sS'_parameter_names'
p19
(S'self'
p20
S'elem'
p21
S'r'
S'v'
S'f'
tp22
sS'_parameter_info'
p23
(dp24
g20
(NNNtp25
sS'r'
(I1
S'array([ 0., 0., 0.] )'
Ntp26
sg21
(NNNtp27
sS'f'
(I1
S'array([ 0., 0., 0.] )'
Ntp28
sS'v'
(I1
S'array([ 0., 0., 0.] )'
Ntp29
ssS'_filename'
p30
S'box/md.py'
p31
sS'_docstring'
p32
S'\n        Initialize atom information.\n        \n        * elem -- the element of atom\n        * r -- position-vector\n        * v -- velocity-vector\n        * f -- force-vector\n        '
p33
sS'_name'
p34
g11
sS'_parent'
p35
g7
sS'_comment_info'
p36
(dp37
sS'_configuration_values'
p38
(dp39
sS'_class_info'
p40
g14
sS'_function_info'
p41
g15
sS'_comments'
p42
S''
sbstp43
sg30
g31
sg32
S"\n    Class for atoms. \n    \n    Atom consists the element information, using the class\n    'Element', but contains also position, velocity etc. variable information.\n    "
p44
sS'_class_member_info'
p45
(lp46
sg34
g6
sg35
g2
sg36
g37
sS'_base_class_info'
p47
(lp48
sg38
(dp49
sg40
g9
sg41
g10
sg42
S''
sbsS'Molecule'
p50
(ihappydoclib.parseinfo.classinfo
ClassInfo
p51
(dp52
g4
((dp53
(dp54
S'input_xyz'
p55
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p56
(dp57
g4
((dp58
(dp59
tp60
sg17
(dp61
sg19
(S'self'
p62
S'file'
p63
tp64
sg23
(dp65
g62
(NNNtp66
sg63
(NNNtp67
ssg30
g31
sg32
S'\n        Read molecule from xyz-file. \n        \n        * file -- the given input xyz-file. It can be either a file name\n        or a file object. If file is a file object the next "frame" is read\n        without rewinding the file.\n        '
p68
sg34
g55
sg35
g51
sg36
g37
sg38
(dp69
sg40
g58
sg41
g59
sg42
S''
sbsS'koe'
p70
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p71
(dp72
g4
((dp73
(dp74
tp75
sg17
(dp76
sg19
(S'self'
p77
S'kk'
p78
tp79
sg23
(dp80
g78
(NNNtp81
sg77
(NNNtp82
ssg30
g31
sg32
S''
sg34
g70
sg35
g51
sg36
g37
sg38
(dp83
sg40
g73
sg41
g74
sg42
S''
sbsS'av_bond_length'
p84
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p85
(dp86
g4
((dp87
(dp88
tp89
sg17
(dp90
sg19
(S'self'
p91
tp92
sg23
(dp93
g91
(NNNtp94
ssg30
g31
sg32
S'\n        Return the average bond length using estimates\n        from pair distribution function.\n        '
p95
sg34
g84
sg35
g51
sg36
g37
sg38
(dp96
sg40
g87
sg41
g88
sg42
S''
sbsS'construct_bonds'
p97
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p98
(dp99
g4
((dp100
(dp101
tp102
sg17
(dp103
sg19
(S'self'
p104
tp105
sg23
(dp106
g104
(NNNtp107
ssg30
g31
sg32
S'\n        Make the bonding list for the molecule.\n        \n        Use estimates for bond lengths from van der Waals radii.\n        Make bond if R<(R_cov,1+R_cov,2)*1.2\n        '
p108
sg34
g97
sg35
g51
sg36
g37
sg38
(dp109
sg40
g100
sg41
g101
sg42
S''
sbsS'output_xyz'
p110
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p111
(dp112
g4
((dp113
(dp114
tp115
sg17
(dp116
sg19
(S'self'
p117
S'file'
p118
tp119
sg23
(dp120
g117
(NNNtp121
sg118
(NNNtp122
ssg30
g31
sg32
S'\n        Write the molecule into a xyz-file. \n        \n        * file -- the output file name or file object. If it is an file\n        object, the molecule is simpy appended as next "frame".\n        '
p123
sg34
g110
sg35
g51
sg36
g37
sg38
(dp124
sg40
g113
sg41
g114
sg42
S''
sbsS'__init__'
p125
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p126
(dp127
g4
((dp128
(dp129
tp130
sg17
(dp131
sg19
(S'self'
p132
S'file'
p133
S'format'
p134
S'efile'
p135
tp136
sg23
(dp137
g132
(NNNtp138
sg135
(I1
S'None'
Ntp139
sg133
(I1
S'None'
Ntp140
sg134
(I1
S"'xyz'"
Ntp141
ssg30
g31
sg32
S"\n        Initialize molecule.\n        \n        * file -- if present, read molecule from this file\n        * format -- format of the given file ('xyz','I_info', or 'dat')\n        * efile -- the path for elements.dat -file used for element info\n        "
p142
sg34
g125
sg35
g51
sg36
g37
sg38
(dp143
sg40
g128
sg41
g129
sg42
S''
sbsS'pair_distr_list'
p144
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p145
(dp146
g4
((dp147
(dp148
tp149
sg17
(dp150
sg19
(S'self'
p151
tp152
sg23
(dp153
g151
(NNNtp154
ssg30
g31
sg32
S'\n        Return the array r_ij=|r_i-r_j| for all pairs a 1-D array.\n        '
p155
sg34
g144
sg35
g51
sg36
g37
sg38
(dp156
sg40
g147
sg41
g148
sg42
S''
sbsS'add_molecule'
p157
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p158
(dp159
g4
((dp160
(dp161
tp162
sg17
(dp163
sg19
(S'self'
p164
S'mol2'
p165
tp166
sg23
(dp167
g164
(NNNtp168
sg165
(NNNtp169
ssg30
g31
sg32
S' \n        Adds the atoms of another molecule to the present one.\n        \n        * mol2 -- the molecule the atoms of which will be added\n        '
p170
sg34
g157
sg35
g51
sg36
g37
sg38
(dp171
sg40
g160
sg41
g161
sg42
S''
sbsS'r2array'
p172
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p173
(dp174
g4
((dp175
(dp176
tp177
sg17
(dp178
sg19
(S'self'
p179
tp180
sg23
(dp181
g179
(NNNtp182
ssg30
g31
sg32
S'\n        Return the atom locations as an array for faster \n        computations.\n        '
p183
sg34
g172
sg35
g51
sg36
g37
sg38
(dp184
sg40
g175
sg41
g176
sg42
S''
sbsS'add'
p185
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p186
(dp187
g4
((dp188
(dp189
tp190
sg17
(dp191
sg19
(S'self'
p192
S'atom'
p193
tp194
sg23
(dp195
g192
(NNNtp196
sg193
(NNNtp197
ssg30
g31
sg32
S'\n        Add atom into the molecule.\n        \n        * atom -- the atom to be added \n        '
p198
sg34
g185
sg35
g51
sg36
g37
sg38
(dp199
sg40
g188
sg41
g189
sg42
S''
sbsS'output_atoms_dat_old'
p200
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p201
(dp202
g4
((dp203
(dp204
tp205
sg17
(dp206
sg19
(S'self'
p207
S'file'
p208
tp209
sg23
(dp210
g207
(NNNtp211
sg208
(NNNtp212
ssg30
g31
sg32
S'\n        Writes the molecule into an atoms.dat file.\n        \n        This is for the older (<5.3 2007) version of atoms.dat.\n        \n        * file -- output file name\n        '
p213
sg34
g200
sg35
g51
sg36
g37
sg38
(dp214
sg40
g203
sg41
g204
sg42
S''
sbsS'scale_r'
p215
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p216
(dp217
g4
((dp218
(dp219
tp220
sg17
(dp221
sg19
(S'self'
p222
S'x'
tp223
sg23
(dp224
S'x'
(NNNtp225
sg222
(NNNtp226
ssg30
g31
sg32
S'\n        Scale all the coordinates.\n        \n        * x -- scaling factor.\n        '
p227
sg34
g215
sg35
g51
sg36
g37
sg38
(dp228
sg40
g218
sg41
g219
sg42
S''
sbsS'__call__'
p229
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p230
(dp231
g4
((dp232
(dp233
tp234
sg17
(dp235
sg19
(S'self'
p236
tp237
sg23
(dp238
g236
(NNNtp239
ssg30
g31
sg32
S'\n        Print some molecule data.\n        \n        Prints locations.\n        '
p240
sg34
g229
sg35
g51
sg36
g37
sg38
(dp241
sg40
g232
sg41
g233
sg42
S''
sbsS'translate'
p242
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p243
(dp244
g4
((dp245
(dp246
tp247
sg17
(dp248
sg19
(S'self'
p249
S'v'
tp250
sg23
(dp251
g249
(NNNtp252
sS'v'
(NNNtp253
ssg30
g31
sg32
S'\n        Translate the molecule.\n        \n        * v -- translate molecule by v\n        '
p254
sg34
g242
sg35
g51
sg36
g37
sg38
(dp255
sg40
g245
sg41
g246
sg42
S''
sbsS'r_cm'
p256
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p257
(dp258
g4
((dp259
(dp260
tp261
sg17
(dp262
sg19
(S'self'
p263
tp264
sg23
(dp265
g263
(NNNtp266
ssg30
g31
sg32
S'\n        Return the center of mass vector of the molecule.\n        '
p267
sg34
g256
sg35
g51
sg36
g37
sg38
(dp268
sg40
g259
sg41
g260
sg42
S''
sbsS'energy_atoms_separated'
p269
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p270
(dp271
g4
((dp272
(dp273
tp274
sg17
(dp275
sg19
(S'self'
p276
tp277
sg23
(dp278
g276
(NNNtp279
ssg30
g31
sg32
S'\n        Return the total energy of separate atoms.\n         \n        Sum of sp energies.\n        '
p280
sg34
g269
sg35
g51
sg36
g37
sg38
(dp281
sg40
g272
sg41
g273
sg42
S''
sbsS'output_atoms_dat'
p282
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p283
(dp284
g4
((dp285
(dp286
tp287
sg17
(dp288
sg19
(S'self'
p289
S'file'
p290
tp291
sg23
(dp292
g289
(NNNtp293
sg290
(NNNtp294
ssg30
g31
sg32
S'\n        Write the molecule into atoms.dat-file.\n        \n        * file -- output file name\n        '
p295
sg34
g282
sg35
g51
sg36
g37
sg38
(dp296
sg40
g285
sg41
g286
sg42
S''
sbsS'nr_bonds'
p297
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p298
(dp299
g4
((dp300
(dp301
tp302
sg17
(dp303
sg19
(S'self'
p304
tp305
sg23
(dp306
g304
(NNNtp307
ssg30
g31
sg32
S'\n        Return the number of bonds (for homonuclear molecule).\n        '
p308
sg34
g297
sg35
g51
sg36
g37
sg38
(dp309
sg40
g300
sg41
g301
sg42
S''
sbsS'input_I_info'
p310
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p311
(dp312
g4
((dp313
(dp314
tp315
sg17
(dp316
sg19
(S'self'
p317
S'file'
p318
tp319
sg23
(dp320
g317
(NNNtp321
sg318
(NNNtp322
ssg30
g31
sg32
S'\n        Reads molecule from I_info -file, used for Cmdft program.\n        \n        * file -- the I_info file for input\n        '
p323
sg34
g310
sg35
g51
sg36
g37
sg38
(dp324
sg40
g313
sg41
g314
sg42
S''
sbsS'input_atoms_dat'
p325
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p326
(dp327
g4
((dp328
(dp329
tp330
sg17
(dp331
sg19
(S'self'
p332
S'file'
p333
tp334
sg23
(dp335
g332
(NNNtp336
sg333
(NNNtp337
ssg30
g31
sg32
S'\n        Read molecule from atoms.dat-file.\n        \n        * file -- the given atoms.dat -file\n        '
p338
sg34
g325
sg35
g51
sg36
g37
sg38
(dp339
sg40
g328
sg41
g329
sg42
S''
sbsS'output_I_info'
p340
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p341
(dp342
g4
((dp343
(dp344
tp345
sg17
(dp346
sg19
(S'self'
p347
S'file'
p348
tp349
sg23
(dp350
g347
(NNNtp351
sg348
(NNNtp352
ssg30
g31
sg32
S'\n        Write the molecule into a I_info-file for Cmdft.\n         \n         * file -- the output file name.\n        '
p353
sg34
g340
sg35
g51
sg36
g37
sg38
(dp354
sg40
g343
sg41
g344
sg42
S''
sbsS'vtk_output'
p355
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p356
(dp357
g4
((dp358
(dp359
tp360
sg17
(dp361
sg19
(S'self'
p362
S'fn'
p363
tp364
sg23
(dp365
g362
(NNNtp366
sg363
(NNNtp367
ssg30
g31
sg32
S"\n        Make a vtk-file of the current molecule.\n        \n        Output of coordinates, charges, velocities, forces, bonds, etc.\n        \n        * fn -- the output file name (e.g. 'molecule.vtk')\n        "
p368
sg34
g355
sg35
g51
sg36
g37
sg38
(dp369
sg40
g358
sg41
g359
sg42
S''
sbsS'move_atom'
p370
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p371
(dp372
g4
((dp373
(dp374
tp375
sg17
(dp376
sg19
(S'self'
p377
S'atom'
p378
S'dr'
p379
tp380
sg23
(dp381
g377
(NNNtp382
sg379
(NNNtp383
sg378
(NNNtp384
ssg30
g31
sg32
S'\n        Translate atom by the vector dr.\n        \n        * atom -- the atom index to be translated. First atom=0.\n        * dr -- the translation vector\n        '
p385
sg34
g370
sg35
g51
sg36
g37
sg38
(dp386
sg40
g373
sg41
g374
sg42
S''
sbsS'pair_distr_function'
p387
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p388
(dp389
g4
((dp390
(dp391
tp392
sg17
(dp393
sg19
(S'self'
p394
S'rmin'
p395
S'rmax'
p396
S'sigma'
p397
tp398
sg23
(dp399
g397
(I1
S'0.7'
Ntp400
sg394
(NNNtp401
sg396
(NNNtp402
sg395
(NNNtp403
ssg30
g31
sg32
S'\n        Return the pair distribution function.\n         \n        * rmin -- the minimum of the function\n        * rmax -- the maximum of the function\n        * sigma -- Gaussian used in the broadening, this is its sigma\n        '
p404
sg34
g387
sg35
g51
sg36
g37
sg38
(dp405
sg40
g390
sg41
g391
sg42
S''
sbstp406
sg30
g31
sg32
S"\n    Class for molecules. \n    \n    Consists of many atoms (using class 'Atom'), and\n    hosts also other additional information such as number of atoms,\n    electrons in the whole molecule, binding info.\n    "
p407
sg45
(lp408
sg34
g50
sg35
g2
sg36
g37
sg47
(lp409
sg38
(dp410
sg40
g53
sg41
g54
sg42
S''
sbsS'Element'
p411
(ihappydoclib.parseinfo.classinfo
ClassInfo
p412
(dp413
g4
((dp414
(dp415
S'energies'
p416
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p417
(dp418
g4
((dp419
(dp420
tp421
sg17
(dp422
sg19
(S'self'
p423
S'ret'
p424
tp425
sg23
(dp426
g423
(NNNtp427
sg424
(NNNtp428
ssg30
g31
sg32
S'\n        Return some characterisics of the electronic structure.\n        \n        * ret -- the returned energy\n        \n            * IE -- ionization energy\n            * EA -- electron affinity\n        '
p429
sg34
g416
sg35
g412
sg36
g37
sg38
(dp430
sg40
g419
sg41
g420
sg42
S''
sbsS'read_element_info'
p431
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p432
(dp433
g4
((dp434
(dp435
tp436
sg17
(dp437
sg19
(S'self'
p438
S'file'
p439
tp440
sg23
(dp441
g438
(NNNtp442
sg439
(NNNtp443
ssg30
g31
sg32
S'\n        Read data for the element from elements.dat-file.\n        \n        * file -- elements.dat -file\n        '
p444
sg34
g431
sg35
g412
sg36
g37
sg38
(dp445
sg40
g434
sg41
g435
sg42
S''
sbsS'sp_occupations'
p446
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p447
(dp448
g4
((dp449
(dp450
tp451
sg17
(dp452
sg19
(S'self'
p453
S'excess_el'
p454
tp455
sg23
(dp456
g453
(NNNtp457
sg454
(I1
S'0'
Ntp458
ssg30
g31
sg32
S'\n        Return the occupations for single particle states with given N_el.\n        \n        * excess_el -- number of excess electrons on element (wrt. neutral)\n        '
p459
sg34
g446
sg35
g412
sg36
g37
sg38
(dp460
sg40
g449
sg41
g450
sg42
S''
sbsS'energy_as_separated'
p461
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p462
(dp463
g4
((dp464
(dp465
tp466
sg17
(dp467
sg19
(S'self'
p468
S'excess_el'
p469
tp470
sg23
(dp471
g468
(NNNtp472
sg469
(I1
S'0'
Ntp473
ssg30
g31
sg32
S'\n        Return the energy of isolated atom .\n        \n        Return sum_i occ_i e_i.\n        \n        * excess_el -- number of excess electrons on element (wrt. neutral)\n        '
p474
sg34
g461
sg35
g412
sg36
g37
sg38
(dp475
sg40
g464
sg41
g465
sg42
S''
sbsS'__call__'
p476
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p477
(dp478
g4
((dp479
(dp480
tp481
sg17
(dp482
sg19
(S'self'
p483
tp484
sg23
(dp485
g483
(NNNtp486
ssg30
g31
sg32
S'\n        Print the element data (__dict__)\n        '
p487
sg34
g476
sg35
g412
sg36
g37
sg38
(dp488
sg40
g479
sg41
g480
sg42
S''
sbsS'__init__'
p489
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p490
(dp491
g4
((dp492
(dp493
tp494
sg17
(dp495
sg19
(S'self'
p496
S'element'
p497
S'fil'
p498
tp499
sg23
(dp500
g496
(NNNtp501
sg498
(I1
S'None'
Ntp502
sg497
(NNNtp503
ssg30
g31
sg32
S'\n        Initialize the element object.\n        \n        At least symbol given, and if file (=elements.dat used for HOTBIT)\n        is present, read more element info from there.\n        \n        Parameters\n            \n            * element -- element symbol\n            \n            * fil -- the path of elements.dat -file\n            \n        '
p504
sg34
g489
sg35
g412
sg36
g37
sg38
(dp505
sg40
g492
sg41
g493
sg42
S''
sbstp506
sg30
g31
sg32
S'\n    Class for elements. \n    \n    Contains element-specific information such\n    as mass, name, ionization potentials etc.\n    '
p507
sg45
(lp508
sg34
g411
sg35
g2
sg36
g37
sg47
(lp509
sg38
(dp510
sg40
g414
sg41
g415
sg42
S''
sbs(dp511
tp512
sS'_import_info'
p513
(ihappydoclib.parseinfo.imports
ImportInfo
p514
(dp515
S'_named_imports'
p516
(dp517
sS'_straight_imports'
p518
(lp519
sbsg30
g31
sg32
S'"""\n    Contain classes related to molecular calculations. \n    \n    Atomic units used throughout unless otherwise stated.\n    \n    Author P. Koskinen 15.9 2006\n    \n"""'
p520
sg34
S'md'
p521
sg35
Nsg36
g37
sg38
(dp522
S'include_comments'
p523
I1
sS'cacheFilePrefix'
p524
S'.happydoc.'
p525
sS'useCache'
p526
I1
sS'docStringFormat'
p527
S'StructuredText'
p528
ssg40
g5
sg41
g511
sg42
S''
sbt.