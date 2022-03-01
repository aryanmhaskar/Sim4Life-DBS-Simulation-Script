import numpy
import s4l_v1.document as document
import s4l_v1.materials.database as database
import s4l_v1.model as model
import s4l_v1.simulation.emlf as emlf
import s4l_v1.units as units
from s4l_v1 import ReleaseVersion
from s4l_v1 import Unit

try:
	# Define the version to use for default values
	ReleaseVersion.set_active(ReleaseVersion.version6_2)
	
	# Creating the simulation
	simulation = emlf.MagnetoQuasiStaticSimulation()
	simulation.Name = "bilateral_5000A"

	# Mapping the components and entities
	component__background = simulation.AllComponents["Background"]
	component__overall_field = simulation.AllComponents["Overall Field"]
	entity__fibula_cancellous_left = model.AllEntities()["Fibula_cancellous_left"]
	entity__heart_lumen = model.AllEntities()["Heart_lumen"]
	entity__femur_cortical_right = model.AllEntities()["Femur_cortical_right"]
	entity__phalanx_media_iv_cortical_right = model.AllEntities()["Phalanx_media_IV_cortical_right"]
	entity__vertebra_cortical_t10 = model.AllEntities()["Vertebra_cortical_T10"]
	entity__salivary_gland = model.AllEntities()["Salivary_gland"]
	entity__vertebra_cortical_c5 = model.AllEntities()["Vertebra_cortical_C5"]
	entity_lf6 = model.AllEntities()["8"]  # "LF 6" is not unique
	entity_sat = model.AllEntities()["SAT"]
	entity__femur_yellow_marrow_right = model.AllEntities()["Femur_yellow_marrow_right"]
	entity__vertebra_cancellous_t5 = model.AllEntities()["Vertebra_cancellous_T5"]
	entity__fibula_cortical_right = model.AllEntities()["Fibula_cortical_right"]
	entity_lf5 = model.AllEntities()["13"]  # "LF 5" is not unique
	entity_lf7 = model.AllEntities()["14"]  # "LF 7" is not unique
	entity__phalanx_distalis_v_cancellous_left = model.AllEntities()["Phalanx_distalis_V_cancellous_left"]
	entity__phalanx_proximalis_iv_cancellous_left = model.AllEntities()["Phalanx_proximalis_IV_cancellous_left"]
	entity__tendon_ligament = model.AllEntities()["Tendon_ligament"]
	entity__phalanx_proximalis_iii_cancellous_left = model.AllEntities()["Phalanx_proximalis_III_cancellous_left"]
	entity__tongue = model.AllEntities()["Tongue"]
	entity__vertebra_cancellous_c6 = model.AllEntities()["Vertebra_cancellous_C6"]
	entity__trachea_wall = model.AllEntities()["Trachea_wall"]
	entity_angled_bilateral_insulation = model.AllEntities()["angled_bilateral_insulation"]
	entity__metacarpus_i_cancellous_right = model.AllEntities()["Metacarpus_I_cancellous_right"]
	entity__femur_cancellous_left = model.AllEntities()["Femur_cancellous_left"]
	entity__vertebra_cancellous_c4 = model.AllEntities()["Vertebra_cancellous_C4"]
	entity__larynx = model.AllEntities()["Larynx"]
	entity__phalanx_proximalis_v_cortical_left = model.AllEntities()["Phalanx_proximalis_V_cortical_left"]
	entity__vertebra_cancellous_c3 = model.AllEntities()["Vertebra_cancellous_C3"]
	entity__humerus_cancellous_left = model.AllEntities()["Humerus_cancellous_left"]
	entity_lf4 = model.AllEntities()["31"]  # "LF 4" is not unique
	entity__bronchus_lumen = model.AllEntities()["Bronchus_lumen"]
	entity__humerus_yellow_marrow_right = model.AllEntities()["Humerus_yellow_marrow_right"]
	entity__phalanx_proximalis_ii_cortical_left = model.AllEntities()["Phalanx_proximalis_II_cortical_left"]
	entity__phalanx_distalis_i_cortical_left = model.AllEntities()["Phalanx_distalis_I_cortical_left"]
	entity__cerebrospinal_fluid = model.AllEntities()["Cerebrospinal_fluid"]
	entity__vertebra_cancellous_l5 = model.AllEntities()["Vertebra_cancellous_L5"]
	entity__phalanx_proximalis_iii_cortical_right = model.AllEntities()["Phalanx_proximalis_III_cortical_right"]
	entity__phalanx_proximalis_i_cancellous_left = model.AllEntities()["Phalanx_proximalis_I_cancellous_left"]
	entity__vertebra_cortical_t11 = model.AllEntities()["Vertebra_cortical_T11"]
	entity__eye_sclera = model.AllEntities()["Eye_sclera"]
	entity_lf3 = model.AllEntities()["42"]  # "LF 3" is not unique
	entity__vertebra_cortical_c1 = model.AllEntities()["Vertebra_cortical_C1"]
	entity__seminal_vesicle = model.AllEntities()["Seminal_vesicle"]
	entity__tibia_cortical_right = model.AllEntities()["Tibia_cortical_right"]
	entity__phalanx_media_iv_cancellous_right = model.AllEntities()["Phalanx_media_IV_cancellous_right"]
	entity__vertebra_cortical_t4 = model.AllEntities()["Vertebra_cortical_T4"]
	entity__humerus_cancellous_right = model.AllEntities()["Humerus_cancellous_right"]
	entity__phalanx_proximalis_ii_cancellous_right = model.AllEntities()["Phalanx_proximalis_II_cancellous_right"]
	entity__cerebellum = model.AllEntities()["Cerebellum"]
	entity__vertebra_cortical_l3 = model.AllEntities()["Vertebra_cortical_L3"]
	entity__ureter = model.AllEntities()["Ureter"]
	entity__muscle = model.AllEntities()["Muscle"]
	entity__phalanx_proximalis_ii_cortical_right = model.AllEntities()["Phalanx_proximalis_II_cortical_right"]
	entity__vertebra_cortical_c6 = model.AllEntities()["Vertebra_cortical_C6"]
	entity__phalanx_distalis_iv_cancellous_left = model.AllEntities()["Phalanx_distalis_IV_cancellous_left"]
	entity__phalanx_proximalis_iv_cortical_right = model.AllEntities()["Phalanx_proximalis_IV_cortical_right"]
	entity__thorax_cortical = model.AllEntities()["Thorax_cortical"]
	entity__humerus_cortical_right = model.AllEntities()["Humerus_cortical_right"]
	entity__ear_skin_left = model.AllEntities()["Ear_skin_left"]
	entity__foot_cortical_left = model.AllEntities()["Foot_cortical_left"]
	entity__vertebra_cancellous_t9 = model.AllEntities()["Vertebra_cancellous_T9"]
	entity__phalanx_proximalis_iii_cancellous_right = model.AllEntities()["Phalanx_proximalis_III_cancellous_right"]
	entity__vertebra_cortical_t1 = model.AllEntities()["Vertebra_cortical_T1"]
	entity__skin = model.AllEntities()["Skin"]
	entity__esophagus_lumen = model.AllEntities()["Esophagus_lumen"]
	entity__vertebra_cortical_l4 = model.AllEntities()["Vertebra_cortical_L4"]
	entity__phalanx_distalis_iv_cortical_right = model.AllEntities()["Phalanx_distalis_IV_cortical_right"]
	entity__esophagus_wall = model.AllEntities()["Esophagus_wall"]
	entity__phalanx_proximalis_iv_cancellous_right = model.AllEntities()["Phalanx_proximalis_IV_cancellous_right"]
	entity__ductus_deferens = model.AllEntities()["Ductus_deferens"]
	entity__trachea_lumen = model.AllEntities()["Trachea_lumen"]
	entity__vertebra_cancellous_t10 = model.AllEntities()["Vertebra_cancellous_T10"]
	entity__hippocampus = model.AllEntities()["Hippocampus"]
	entity__phalanx_media_ii_cancellous_left = model.AllEntities()["Phalanx_media_II_cancellous_left"]
	entity__vertebra_cancellous_t2 = model.AllEntities()["Vertebra_cancellous_T2"]
	entity__femur_cortical_left = model.AllEntities()["Femur_cortical_left"]
	entity__vertebra_cancellous_c7 = model.AllEntities()["Vertebra_cancellous_C7"]
	entity__phalanx_proximalis_iv_cortical_left = model.AllEntities()["Phalanx_proximalis_IV_cortical_left"]
	entity__bronchus_wall = model.AllEntities()["Bronchus_wall"]
	entity__ulna_cortical_left = model.AllEntities()["Ulna_cortical_left"]
	entity_lf7_1 = model.AllEntities()["82"]  # "LF 7" is not unique
	entity__vertebra_cortical_l5 = model.AllEntities()["Vertebra_cortical_L5"]
	entity__lung = model.AllEntities()["Lung"]
	entity__phalanx_distalis_ii_cancellous_left = model.AllEntities()["Phalanx_distalis_II_cancellous_left"]
	entity__hyoid_cortical = model.AllEntities()["Hyoid_cortical"]
	entity__phalanx_distalis_ii_cortical_left = model.AllEntities()["Phalanx_distalis_II_cortical_left"]
	entity__phalanx_distalis_v_cortical_left = model.AllEntities()["Phalanx_distalis_V_cortical_left"]
	entity__diaphragm = model.AllEntities()["Diaphragm"]
	entity__urine = model.AllEntities()["Urine"]
	entity__phalanx_media_iv_cancellous_left = model.AllEntities()["Phalanx_media_IV_cancellous_left"]
	entity__pons = model.AllEntities()["Pons"]
	entity__intervertebral_disc = model.AllEntities()["Intervertebral_disc"]
	entity__phalanx_proximalis_iii_cortical_left = model.AllEntities()["Phalanx_proximalis_III_cortical_left"]
	entity__phalanx_media_v_cortical_right = model.AllEntities()["Phalanx_media_V_cortical_right"]
	entity__ear_cartilage_right = model.AllEntities()["Ear_cartilage_right"]
	entity__vertebra_cancellous_c1 = model.AllEntities()["Vertebra_cancellous_C1"]
	entity__gallbladder_wall = model.AllEntities()["Gallbladder_wall"]
	entity__skull_cortical = model.AllEntities()["Skull_cortical"]
	entity__vertebra_cortical_l2 = model.AllEntities()["Vertebra_cortical_L2"]
	entity_lf8 = model.AllEntities()["101"]  # "LF 8" is not unique
	entity__vertebra_cortical_os_sacrum_coccyx = model.AllEntities()["Vertebra_cortical_os_sacrum_coccyx"]
	entity_lf2 = model.AllEntities()["103"]  # "LF 2" is not unique
	entity__metacarpus_i_cortical_left = model.AllEntities()["Metacarpus_I_cortical_left"]
	entity__phalanx_distalis_ii_cancellous_right = model.AllEntities()["Phalanx_distalis_II_cancellous_right"]
	entity__large_intestine_wall = model.AllEntities()["Large_intestine_wall"]
	entity__meniscus_right = model.AllEntities()["Meniscus_right"]
	entity__phalanx_proximalis_ii_cancellous_left = model.AllEntities()["Phalanx_proximalis_II_cancellous_left"]
	entity__commissura_anterior = model.AllEntities()["Commissura_anterior"]
	entity__vertebra_cancellous_t4 = model.AllEntities()["Vertebra_cancellous_T4"]
	entity_lf2_1 = model.AllEntities()["111"]  # "LF 2" is not unique
	entity__phalanx_distalis_iv_cortical_left = model.AllEntities()["Phalanx_distalis_IV_cortical_left"]
	entity__vertebra_cancellous_l1 = model.AllEntities()["Vertebra_cancellous_L1"]
	entity__phalanx_media_iv_cortical_left = model.AllEntities()["Phalanx_media_IV_cortical_left"]
	entity__phalanx_media_v_cancellous_right = model.AllEntities()["Phalanx_media_V_cancellous_right"]
	entity__ulna_cancellous_right = model.AllEntities()["Ulna_cancellous_right"]
	entity__vertebra_cancellous_l3 = model.AllEntities()["Vertebra_cancellous_L3"]
	entity__tibia_cancellous_right = model.AllEntities()["Tibia_cancellous_right"]
	entity__vertebra_cancellous_t1 = model.AllEntities()["Vertebra_cancellous_T1"]
	entity__patella_cancellous_left = model.AllEntities()["Patella_cancellous_left"]
	entity__phalanx_media_iii_cancellous_left = model.AllEntities()["Phalanx_media_III_cancellous_left"]
	entity__phalanx_distalis_ii_cortical_right = model.AllEntities()["Phalanx_distalis_II_cortical_right"]
	entity__small_intestine_lumen = model.AllEntities()["Small_intestine_lumen"]
	entity__vertebra_cortical_t9 = model.AllEntities()["Vertebra_cortical_T9"]
	entity__eye_vitreous_humor = model.AllEntities()["Eye_vitreous_humor"]
	entity_lf4_1 = model.AllEntities()["127"]  # "LF 4" is not unique
	entity__liver = model.AllEntities()["Liver"]
	entity__tibia_cortical_left = model.AllEntities()["Tibia_cortical_left"]
	entity__skull_cancellous = model.AllEntities()["Skull_cancellous"]
	entity__phalanx_proximalis_v_cortical_right = model.AllEntities()["Phalanx_proximalis_V_cortical_right"]
	entity__vertebra_cortical_c2 = model.AllEntities()["Vertebra_cortical_C2"]
	entity__mandible_cancellous = model.AllEntities()["Mandible_cancellous"]
	entity__fibula_cancellous_right = model.AllEntities()["Fibula_cancellous_right"]
	entity__vertebra_cancellous_l4 = model.AllEntities()["Vertebra_cancellous_L4"]
	entity__heart_muscle = model.AllEntities()["Heart_muscle"]
	entity_lf1 = model.AllEntities()["137"]  # "LF 1" is not unique
	entity__carpalia__metacarpalia_cortical_left = model.AllEntities()["Carpalia_Metacarpalia_cortical_left"]
	entity__bladder_wall = model.AllEntities()["Bladder_wall"]
	entity__tooth = model.AllEntities()["Tooth"]
	entity__phalanx_distalis_i_cancellous_left = model.AllEntities()["Phalanx_distalis_I_cancellous_left"]
	entity__vertebra_cancellous_c2 = model.AllEntities()["Vertebra_cancellous_C2"]
	entity__vertebra_cortical_c4 = model.AllEntities()["Vertebra_cortical_C4"]
	entity__eye_lens = model.AllEntities()["Eye_lens"]
	entity__mucosa = model.AllEntities()["Mucosa"]
	entity__epididymis = model.AllEntities()["Epididymis"]
	entity__vertebra_cortical_t5 = model.AllEntities()["Vertebra_cortical_T5"]
	entity__phalanx_distalis_iii_cortical_left = model.AllEntities()["Phalanx_distalis_III_cortical_left"]
	entity__vertebra_cancellous_t7 = model.AllEntities()["Vertebra_cancellous_T7"]
	entity__vertebra_cancellous_t3 = model.AllEntities()["Vertebra_cancellous_T3"]
	entity__thyroid_gland = model.AllEntities()["Thyroid_gland"]
	entity__pineal_body = model.AllEntities()["Pineal_body"]
	entity__vertebra_cancellous_l2 = model.AllEntities()["Vertebra_cancellous_L2"]
	entity__lymph_node = model.AllEntities()["Lymph_node"]
	entity__tibia_cancellous_left = model.AllEntities()["Tibia_cancellous_left"]
	entity__fibula_yellow_marrow_left = model.AllEntities()["Fibula_yellow_marrow_left"]
	entity__corpus_callosum = model.AllEntities()["Corpus_callosum"]
	entity__carpalia__metacarpalia_cancellous_left = model.AllEntities()["Carpalia_Metacarpalia_cancellous_left"]
	entity__phalanx_distalis_v_cortical_right = model.AllEntities()["Phalanx_distalis_V_cortical_right"]
	entity__radius_cortical_right = model.AllEntities()["Radius_cortical_right"]
	entity__phalanx_distalis_iii_cancellous_right = model.AllEntities()["Phalanx_distalis_III_cancellous_right"]
	entity__spinal_cord = model.AllEntities()["Spinal_cord"]
	entity__vertebra_cortical_c3 = model.AllEntities()["Vertebra_cortical_C3"]
	entity__ear_cartilage_left = model.AllEntities()["Ear_cartilage_left"]
	entity__pelvis_cortical = model.AllEntities()["Pelvis_cortical"]
	entity__foot_cortical_right = model.AllEntities()["Foot_cortical_right"]
	entity__penis = model.AllEntities()["Penis"]
	entity__ear_skin_right = model.AllEntities()["Ear_skin_right"]
	entity__mandible_cortical = model.AllEntities()["Mandible_cortical"]
	entity_lf1_1 = model.AllEntities()["LF1"]
	entity__phalanx_media_iii_cortical_left = model.AllEntities()["Phalanx_media_III_cortical_left"]
	entity__vertebra_cortical_t7 = model.AllEntities()["Vertebra_cortical_T7"]
	entity__spleen = model.AllEntities()["Spleen"]
	entity__commissura_posterior = model.AllEntities()["Commissura_posterior"]
	entity__testis = model.AllEntities()["Testis"]
	entity__cerebrum_white_matter = model.AllEntities()["Cerebrum_white_matter"]
	entity__patella_cortical_right = model.AllEntities()["Patella_cortical_right"]
	entity__foot_cancellous_left = model.AllEntities()["Foot_cancellous_left"]
	entity__phalanx_media_iii_cancellous_right = model.AllEntities()["Phalanx_media_III_cancellous_right"]
	entity__carpalia__metacarpalia_cortical_right = model.AllEntities()["Carpalia_Metacarpalia_cortical_right"]
	entity__vertebra_cortical_t3 = model.AllEntities()["Vertebra_cortical_T3"]
	entity__tibia_yellow_marrow_left = model.AllEntities()["Tibia_yellow_marrow_left"]
	entity__stomach_wall = model.AllEntities()["Stomach_wall"]
	entity__vertebra_cortical_l1 = model.AllEntities()["Vertebra_cortical_L1"]
	entity__phalanx_media_ii_cortical_left = model.AllEntities()["Phalanx_media_II_cortical_left"]
	entity__fibula_cortical_left = model.AllEntities()["Fibula_cortical_left"]
	entity_lf6_1 = model.AllEntities()["188"]  # "LF 6" is not unique
	entity__metacarpus_i_cancellous_left = model.AllEntities()["Metacarpus_I_cancellous_left"]
	entity__patella_cortical_left = model.AllEntities()["Patella_cortical_left"]
	entity__phalanx_distalis_iii_cortical_right = model.AllEntities()["Phalanx_distalis_III_cortical_right"]
	entity__nerve = model.AllEntities()["Nerve"]
	entity__radius_yellow_marrow_left = model.AllEntities()["Radius_yellow_marrow_left"]
	entity__thalamus = model.AllEntities()["Thalamus"]
	entity__radius_cancellous_left = model.AllEntities()["Radius_cancellous_left"]
	entity__phalanx_media_v_cortical_left = model.AllEntities()["Phalanx_media_V_cortical_left"]
	entity__radius_cancellous_right = model.AllEntities()["Radius_cancellous_right"]
	entity__midbrain = model.AllEntities()["Midbrain"]
	entity__thorax_cancellous = model.AllEntities()["Thorax_cancellous"]
	entity__vertebra_cortical_t2 = model.AllEntities()["Vertebra_cortical_T2"]
	entity__phalanx_distalis_i_cortical_right = model.AllEntities()["Phalanx_distalis_I_cortical_right"]
	entity__hyoid_cancellous = model.AllEntities()["Hyoid_cancellous"]
	entity__phalanx_media_iii_cortical_right = model.AllEntities()["Phalanx_media_III_cortical_right"]
	entity__patella_cancellous_right = model.AllEntities()["Patella_cancellous_right"]
	entity__humerus_cortical_left = model.AllEntities()["Humerus_cortical_left"]
	entity__fibula_yellow_marrow_right = model.AllEntities()["Fibula_yellow_marrow_right"]
	entity__foot_cancellous_right = model.AllEntities()["Foot_cancellous_right"]
	entity__vertebra_cancellous_t12 = model.AllEntities()["Vertebra_cancellous_T12"]
	entity__phalanx_distalis_iii_cancellous_left = model.AllEntities()["Phalanx_distalis_III_cancellous_left"]
	entity__phalanx_proximalis_v_cancellous_left = model.AllEntities()["Phalanx_proximalis_V_cancellous_left"]
	entity_lf8_1 = model.AllEntities()["212"]  # "LF 8" is not unique
	entity__humerus_yellow_marrow_left = model.AllEntities()["Humerus_yellow_marrow_left"]
	entity__phalanx_proximalis_v_cancellous_right = model.AllEntities()["Phalanx_proximalis_V_cancellous_right"]
	entity__vertebra_cortical_t6 = model.AllEntities()["Vertebra_cortical_T6"]
	entity__phalanx_distalis_iv_cancellous_right = model.AllEntities()["Phalanx_distalis_IV_cancellous_right"]
	entity__vertebra_cancellous_os_sacrum_coccyx = model.AllEntities()["Vertebra_cancellous_os_sacrum_coccyx"]
	entity__phalanx_media_v_cancellous_left = model.AllEntities()["Phalanx_media_V_cancellous_left"]
	entity__ulna_cancellous_left = model.AllEntities()["Ulna_cancellous_left"]
	entity__pelvis_cancellous = model.AllEntities()["Pelvis_cancellous"]
	entity__air_internal = model.AllEntities()["Air_internal"]
	entity__pancreas = model.AllEntities()["Pancreas"]
	entity__fat = model.AllEntities()["Fat"]
	entity__phalanx_distalis_i_cancellous_right = model.AllEntities()["Phalanx_distalis_I_cancellous_right"]
	entity__meniscus_left = model.AllEntities()["Meniscus_left"]
	entity__phalanx_media_ii_cortical_right = model.AllEntities()["Phalanx_media_II_cortical_right"]
	entity__ulna_yellow_marrow_right = model.AllEntities()["Ulna_yellow_marrow_right"]
	entity_lf3_1 = model.AllEntities()["229"]  # "LF 3" is not unique
	entity__vertebra_cancellous_t11 = model.AllEntities()["Vertebra_cancellous_T11"]
	entity__dura_mater = model.AllEntities()["Dura_mater"]
	entity__stomach_lumen = model.AllEntities()["Stomach_lumen"]
	entity__tibia_yellow_marrow_right = model.AllEntities()["Tibia_yellow_marrow_right"]
	entity__radius_yellow_marrow_right = model.AllEntities()["Radius_yellow_marrow_right"]
	entity__vertebra_cancellous_t8 = model.AllEntities()["Vertebra_cancellous_T8"]
	entity__cartilage = model.AllEntities()["Cartilage"]
	entity__small_intestine_wall = model.AllEntities()["Small_intestine_wall"]
	entity_lf5_1 = model.AllEntities()["241"]  # "LF 5" is not unique
	entity__urethra = model.AllEntities()["Urethra"]
	entity__metacarpus_i_cortical_right = model.AllEntities()["Metacarpus_I_cortical_right"]
	entity__phalanx_proximalis_i_cortical_left = model.AllEntities()["Phalanx_proximalis_I_cortical_left"]
	entity__phalanx_media_ii_cancellous_right = model.AllEntities()["Phalanx_media_II_cancellous_right"]
	entity__hypophysis = model.AllEntities()["Hypophysis"]
	entity__vertebra_cortical_t12 = model.AllEntities()["Vertebra_cortical_T12"]
	entity__gallbladder_bile = model.AllEntities()["Gallbladder_bile"]
	entity__hypothalamus = model.AllEntities()["Hypothalamus"]
	entity__radius_cortical_left = model.AllEntities()["Radius_cortical_left"]
	entity__vertebra_cortical_t8 = model.AllEntities()["Vertebra_cortical_T8"]
	entity__phalanx_proximalis_i_cortical_right = model.AllEntities()["Phalanx_proximalis_I_cortical_right"]
	entity_lf9 = model.AllEntities()["LF 9"]
	entity__ulna_yellow_marrow_left = model.AllEntities()["Ulna_yellow_marrow_left"]
	entity__vertebra_cortical_c7 = model.AllEntities()["Vertebra_cortical_C7"]
	entity__femur_cancellous_right = model.AllEntities()["Femur_cancellous_right"]
	entity__eye_cornea = model.AllEntities()["Eye_cornea"]
	entity__vertebra_cancellous_t6 = model.AllEntities()["Vertebra_cancellous_T6"]
	entity__kidney_cortex = model.AllEntities()["Kidney_cortex"]
	entity__medulla_oblongata = model.AllEntities()["Medulla_oblongata"]
	entity_angled_bilateral_conductive = model.AllEntities()["angled_bilateral_conductive"]
	entity__carpalia__metacarpalia_cancellous_right = model.AllEntities()["Carpalia_Metacarpalia_cancellous_right"]
	entity__artery = model.AllEntities()["Artery"]
	entity_lf1_2 = model.AllEntities()["264"]  # "LF 1" is not unique
	entity__prostate = model.AllEntities()["Prostate"]
	entity__cerebrum_grey_matter = model.AllEntities()["Cerebrum_grey_matter"]
	entity__kidney_medulla = model.AllEntities()["Kidney_medulla"]
	entity__phalanx_distalis_v_cancellous_right = model.AllEntities()["Phalanx_distalis_V_cancellous_right"]
	entity__large_intestine_lumen = model.AllEntities()["Large_intestine_lumen"]
	entity__vein = model.AllEntities()["Vein"]
	entity__adrenal_gland = model.AllEntities()["Adrenal_gland"]
	entity__femur_yellow_marrow_left = model.AllEntities()["Femur_yellow_marrow_left"]
	entity__phalanx_proximalis_i_cancellous_right = model.AllEntities()["Phalanx_proximalis_I_cancellous_right"]
	entity__vertebra_cancellous_c5 = model.AllEntities()["Vertebra_cancellous_C5"]
	entity__ulna_cortical_right = model.AllEntities()["Ulna_cortical_right"]

	# Editing QuasiStaticSetupSettings "Setup"
	quasi_static_setup_settings = [x for x in simulation.AllSettings if isinstance(x, emlf.QuasiStaticSetupSettings) and x.Name == "Setup"][0]
	quasi_static_setup_settings.Frequency = 2500.0, units.Hz

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__urine]
	mat = database["IT'IS 4.0"]["Urine"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Urine"
		material_settings.MassDensity = 1023.61320427124, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 1.7500000000000002, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 49.95
	material_settings.ElectricProps.Conductivity = 1.7500000000000002, Unit("S/m")
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__tooth]
	mat = database["IT'IS 4.0"]["Tooth"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Tooth"
		material_settings.MassDensity = 2180.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.02026373356995603, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 1435.1836194179505
	material_settings.ElectricProps.Conductivity = 0.02026373356995603, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 1435.1836194179505
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__thyroid_gland]
	mat = database["IT'IS 4.0"]["Thyroid Gland"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Thyroid Gland"
		material_settings.MassDensity = 1050.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.526414671040721, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 28024.231539934775
	material_settings.ElectricProps.Conductivity = 0.526414671040721, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 28024.231539934775
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__trachea_lumen]
	mat = database["IT'IS 4.0"]["Trachea Lumen"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Trachea Lumen"
		material_settings.MassDensity = 1.16409155293818, Unit("kg/m^3")
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__trachea_wall]
	mat = database["IT'IS 4.0"]["Trachea"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Trachea"
		material_settings.MassDensity = 1080.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.3022184272627871, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 42428.98364106
	material_settings.ElectricProps.Conductivity = 0.3022184272627871, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 42428.98364106
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__testis]
	mat = database["IT'IS 4.0"]["Testis"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Testis"
		material_settings.MassDensity = 1082.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.42641623184451083, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 30522.402399893053
	material_settings.ElectricProps.Conductivity = 0.42641623184451083, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 30522.402399893053
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__thalamus]
	mat = database["IT'IS 4.0"]["Thalamus"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Thalamus"
		material_settings.MassDensity = 1044.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.10431635344104477, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 78103.94438829373
	material_settings.ElectricProps.Conductivity = 0.10431635344104477, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 78103.94438829373
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__carpalia__metacarpalia_cancellous_left, entity__carpalia__metacarpalia_cancellous_right, entity__femur_cancellous_left, entity__femur_cancellous_right, entity__fibula_cancellous_left, entity__fibula_cancellous_right, entity__foot_cancellous_left, entity__foot_cancellous_right, entity__humerus_cancellous_left, entity__humerus_cancellous_right, entity__hyoid_cancellous, entity__mandible_cancellous, entity__metacarpus_i_cancellous_left, entity__metacarpus_i_cancellous_right, entity__patella_cancellous_left, entity__patella_cancellous_right, entity__pelvis_cancellous, entity__phalanx_distalis_i_cancellous_left, entity__phalanx_distalis_i_cancellous_right, entity__phalanx_distalis_ii_cancellous_left, entity__phalanx_distalis_ii_cancellous_right, entity__phalanx_distalis_iii_cancellous_left, entity__phalanx_distalis_iii_cancellous_right, entity__phalanx_distalis_iv_cancellous_left, entity__phalanx_distalis_iv_cancellous_right, entity__phalanx_distalis_v_cancellous_left, entity__phalanx_distalis_v_cancellous_right, entity__phalanx_media_ii_cancellous_left, entity__phalanx_media_ii_cancellous_right, entity__phalanx_media_iii_cancellous_left, entity__phalanx_media_iii_cancellous_right, entity__phalanx_media_iv_cancellous_left, entity__phalanx_media_iv_cancellous_right, entity__phalanx_media_v_cancellous_left, entity__phalanx_media_v_cancellous_right, entity__phalanx_proximalis_i_cancellous_left, entity__phalanx_proximalis_i_cancellous_right, entity__phalanx_proximalis_ii_cancellous_left, entity__phalanx_proximalis_ii_cancellous_right, entity__phalanx_proximalis_iii_cancellous_left, entity__phalanx_proximalis_iii_cancellous_right, entity__phalanx_proximalis_iv_cancellous_left, entity__phalanx_proximalis_iv_cancellous_right, entity__phalanx_proximalis_v_cancellous_left, entity__phalanx_proximalis_v_cancellous_right, entity__radius_cancellous_left, entity__radius_cancellous_right, entity__skull_cancellous, entity__thorax_cancellous, entity__tibia_cancellous_left, entity__tibia_cancellous_right, entity__ulna_cancellous_left, entity__ulna_cancellous_right, entity__vertebra_cancellous_c1, entity__vertebra_cancellous_c2, entity__vertebra_cancellous_c3, entity__vertebra_cancellous_c4, entity__vertebra_cancellous_c5, entity__vertebra_cancellous_c6, entity__vertebra_cancellous_c7, entity__vertebra_cancellous_l1, entity__vertebra_cancellous_l2, entity__vertebra_cancellous_l3, entity__vertebra_cancellous_l4, entity__vertebra_cancellous_l5, entity__vertebra_cancellous_os_sacrum_coccyx, entity__vertebra_cancellous_t1, entity__vertebra_cancellous_t10, entity__vertebra_cancellous_t11, entity__vertebra_cancellous_t12, entity__vertebra_cancellous_t2, entity__vertebra_cancellous_t3, entity__vertebra_cancellous_t4, entity__vertebra_cancellous_t5, entity__vertebra_cancellous_t6, entity__vertebra_cancellous_t7, entity__vertebra_cancellous_t8, entity__vertebra_cancellous_t9]
	mat = database["IT'IS 4.0"]["Bone (Cancellous)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Bone (Cancellous)"
		material_settings.MassDensity = 1178.33333333333, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.08195888706381473, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 5605.148455208243
	material_settings.ElectricProps.Conductivity = 0.08195888706381473, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 5605.148455208243
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__commissura_anterior]
	mat = database["IT'IS 4.0"]["Commissura Anterior"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Commissura Anterior"
		material_settings.MassDensity = 1041.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.06453647163317279, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 34281.99510945726
	material_settings.ElectricProps.Conductivity = 0.06453647163317279, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 34281.99510945726
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__carpalia__metacarpalia_cortical_left, entity__carpalia__metacarpalia_cortical_right, entity__femur_cortical_left, entity__femur_cortical_right, entity__fibula_cortical_left, entity__fibula_cortical_right, entity__foot_cortical_left, entity__foot_cortical_right, entity__humerus_cortical_left, entity__humerus_cortical_right, entity__hyoid_cortical, entity__mandible_cortical, entity__metacarpus_i_cortical_left, entity__metacarpus_i_cortical_right, entity__patella_cortical_left, entity__patella_cortical_right, entity__pelvis_cortical, entity__phalanx_distalis_i_cortical_left, entity__phalanx_distalis_i_cortical_right, entity__phalanx_distalis_ii_cortical_left, entity__phalanx_distalis_ii_cortical_right, entity__phalanx_distalis_iii_cortical_left, entity__phalanx_distalis_iii_cortical_right, entity__phalanx_distalis_iv_cortical_left, entity__phalanx_distalis_iv_cortical_right, entity__phalanx_distalis_v_cortical_left, entity__phalanx_distalis_v_cortical_right, entity__phalanx_media_ii_cortical_left, entity__phalanx_media_ii_cortical_right, entity__phalanx_media_iii_cortical_left, entity__phalanx_media_iii_cortical_right, entity__phalanx_media_iv_cortical_left, entity__phalanx_media_iv_cortical_right, entity__phalanx_media_v_cortical_left, entity__phalanx_media_v_cortical_right, entity__phalanx_proximalis_i_cortical_left, entity__phalanx_proximalis_i_cortical_right, entity__phalanx_proximalis_ii_cortical_left, entity__phalanx_proximalis_ii_cortical_right, entity__phalanx_proximalis_iii_cortical_left, entity__phalanx_proximalis_iii_cortical_right, entity__phalanx_proximalis_iv_cortical_left, entity__phalanx_proximalis_iv_cortical_right, entity__phalanx_proximalis_v_cortical_left, entity__phalanx_proximalis_v_cortical_right, entity__radius_cortical_left, entity__radius_cortical_right, entity__skull_cortical, entity__thorax_cortical, entity__tibia_cortical_left, entity__tibia_cortical_right, entity__ulna_cortical_left, entity__ulna_cortical_right, entity__vertebra_cortical_c1, entity__vertebra_cortical_c2, entity__vertebra_cortical_c3, entity__vertebra_cortical_c4, entity__vertebra_cortical_c5, entity__vertebra_cortical_c6, entity__vertebra_cortical_c7, entity__vertebra_cortical_l1, entity__vertebra_cortical_l2, entity__vertebra_cortical_l3, entity__vertebra_cortical_l4, entity__vertebra_cortical_l5, entity__vertebra_cortical_os_sacrum_coccyx, entity__vertebra_cortical_t1, entity__vertebra_cortical_t10, entity__vertebra_cortical_t11, entity__vertebra_cortical_t12, entity__vertebra_cortical_t2, entity__vertebra_cortical_t3, entity__vertebra_cortical_t4, entity__vertebra_cortical_t5, entity__vertebra_cortical_t6, entity__vertebra_cortical_t7, entity__vertebra_cortical_t8, entity__vertebra_cortical_t9]
	mat = database["IT'IS 4.0"]["Bone (Cortical)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Bone (Cortical)"
		material_settings.MassDensity = 1908.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.02026373356995603, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 1435.1836194179505
	material_settings.ElectricProps.Conductivity = 0.02026373356995603, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 1435.1836194179505
	simulation.Add(material_settings, components)

	# Editing MaterialSettings "Air"
	material_settings = [x for x in simulation.AllSettings if isinstance(x, emlf.MaterialSettings) and x.Name == "Air"][0]
	mat = database["IT'IS 4.0"]["Air"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		components = [component__background, entity__air_internal]
		simulation.Add(material_settings, components)
		material_settings.MassDensity = 1.16409155293818, Unit("kg/m^3")

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity_angled_bilateral_conductive]
	mat = database["Generic 1.1"]["Platinium"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Platinium"
		material_settings.ElectricProps.Conductivity = 9520000.0, Unit("S/m")
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity_angled_bilateral_insulation]
	mat = database["Generic 1.1"]["Polyethylene"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Polyethylene"
		material_settings.ElectricProps.Conductivity = 0.0005, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 2.25
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__bladder_wall]
	mat = database["IT'IS 4.0"]["Urinary Bladder Wall"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Urinary Bladder Wall"
		material_settings.MassDensity = 1086.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.20972333484218833, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 25405.245884569602
	material_settings.ElectricProps.Conductivity = 0.20972333484218833, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 25405.245884569602
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__artery, entity__vein]
	mat = database["IT'IS 4.0"]["Blood"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Blood"
		material_settings.MassDensity = 1049.75, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.7000027557815645, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 5256.784257405785
	material_settings.ElectricProps.Conductivity = 0.7000027557815645, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 5256.784257405785
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__adrenal_gland]
	mat = database["IT'IS 4.0"]["Adrenal Gland"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Adrenal Gland"
		material_settings.MassDensity = 1027.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.6200000942781406, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 74.78074993387574
	material_settings.ElectricProps.Conductivity = 0.6200000942781406, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 74.78074993387574
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__cartilage, entity__ear_cartilage_left, entity__ear_cartilage_right]
	mat = database["IT'IS 4.0"]["Cartilage"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Cartilage"
		material_settings.MassDensity = 1099.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.1751144565321121, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 11324.322841663925
	material_settings.ElectricProps.Conductivity = 0.1751144565321121, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 11324.322841663925
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__cerebrum_grey_matter]
	mat = database["IT'IS 4.0"]["Brain (Grey Matter)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Brain (Grey Matter)"
		material_settings.MassDensity = 1044.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.10431635344104477, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 78103.94438829373
	material_settings.ElectricProps.Conductivity = 0.10431635344104477, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 78103.94438829373
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__commissura_posterior]
	mat = database["IT'IS 4.0"]["Commissura Posterior"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Commissura Posterior"
		material_settings.MassDensity = 1041.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.06453647163317279, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 34281.99510945726
	material_settings.ElectricProps.Conductivity = 0.06453647163317279, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 34281.99510945726
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__femur_yellow_marrow_left, entity__femur_yellow_marrow_right, entity__fibula_yellow_marrow_left, entity__fibula_yellow_marrow_right, entity__humerus_yellow_marrow_left, entity__humerus_yellow_marrow_right, entity__radius_yellow_marrow_left, entity__radius_yellow_marrow_right, entity__tibia_yellow_marrow_left, entity__tibia_yellow_marrow_right, entity__ulna_yellow_marrow_left, entity__ulna_yellow_marrow_right]
	mat = database["IT'IS 4.0"]["Bone Marrow (Yellow)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Bone Marrow (Yellow)"
		material_settings.MassDensity = 980.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.0029418304973174193, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 2353.0951445151163
	material_settings.ElectricProps.Conductivity = 0.0029418304973174193, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 2353.0951445151163
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__cerebrum_white_matter, entity__corpus_callosum]
	mat = database["IT'IS 4.0"]["Brain (White Matter)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Brain (White Matter)"
		material_settings.MassDensity = 1041.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.06453647163317279, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 34281.99510945726
	material_settings.ElectricProps.Conductivity = 0.06453647163317279, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 34281.99510945726
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__bronchus_wall]
	mat = database["IT'IS 4.0"]["Bronchi"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Bronchi"
		material_settings.MassDensity = 1101.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.3022184272627871, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 42428.98364106
	material_settings.ElectricProps.Conductivity = 0.3022184272627871, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 42428.98364106
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__cerebellum]
	mat = database["IT'IS 4.0"]["Cerebellum"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Cerebellum"
		material_settings.MassDensity = 1045.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.12431638861961161, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 78398.8834380823
	material_settings.ElectricProps.Conductivity = 0.12431638861961161, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 78398.8834380823
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__bronchus_lumen]
	mat = database["IT'IS 4.0"]["Bronchi lumen"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Bronchi lumen"
		material_settings.MassDensity = 1.16409155293818, Unit("kg/m^3")
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__cerebrospinal_fluid]
	mat = database["IT'IS 4.0"]["Cerebrospinal Fluid"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Cerebrospinal Fluid"
		material_settings.MassDensity = 1007.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 2.0000000001445914, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 108.99999374511782
	material_settings.ElectricProps.Conductivity = 2.0000000001445914, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 108.99999374511782
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__ear_skin_left, entity__ear_skin_right, entity__skin]
	mat = database["IT'IS 4.0"]["Skin"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Skin"
		material_settings.MassDensity = 1109.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.00020033763126594506, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 1135.2053012854426
	material_settings.ElectricProps.Conductivity = 0.00020033763126594506, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 1135.2053012854426
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__esophagus_wall]
	mat = database["IT'IS 4.0"]["Esophagus"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Esophagus"
		material_settings.MassDensity = 1040.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.5264137798165603, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 27530.286281412
	material_settings.ElectricProps.Conductivity = 0.5264137798165603, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 27530.286281412
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__esophagus_lumen]
	mat = database["IT'IS 4.0"]["Esophagus Lumen"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Esophagus Lumen"
		material_settings.MassDensity = 1.16409155293818, Unit("kg/m^3")
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__eye_cornea]
	mat = database["IT'IS 4.0"]["Eye (Cornea)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Eye (Cornea)"
		material_settings.MassDensity = 1061.645540354, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.42557920368327823, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 88636.14449994982
	material_settings.ElectricProps.Conductivity = 0.42557920368327823, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 88636.14449994982
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__diaphragm]
	mat = database["IT'IS 4.0"]["Diaphragm"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Diaphragm"
		material_settings.MassDensity = 1090.4, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__dura_mater]
	mat = database["IT'IS 4.0"]["Dura"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Dura"
		material_settings.MassDensity = 1174.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.5009723169540081, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 2742.6942171337164
	material_settings.ElectricProps.Conductivity = 0.5009723169540081, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 2742.6942171337164
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__ductus_deferens]
	mat = database["IT'IS 4.0"]["Ductus Deferens"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Ductus Deferens"
		material_settings.MassDensity = 1101.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.3096877839238362, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 40886.44452278335
	material_settings.ElectricProps.Conductivity = 0.3096877839238362, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 40886.44452278335
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__epididymis]
	mat = database["IT'IS 4.0"]["Epididymis"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Epididymis"
		material_settings.MassDensity = 1082.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.42641623184451083, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 30522.402399893053
	material_settings.ElectricProps.Conductivity = 0.42641623184451083, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 30522.402399893053
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__fat]
	mat = database["IT'IS 4.0"]["Fat"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Fat"
		material_settings.MassDensity = 911.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.04242149292939708, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 6425.317623083546
	material_settings.ElectricProps.Conductivity = 0.04242149292939708, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 6425.317623083546
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__hippocampus]
	mat = database["IT'IS 4.0"]["Hippocampus"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Hippocampus"
		material_settings.MassDensity = 1044.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.10431635344104477, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 78103.94438829373
	material_settings.ElectricProps.Conductivity = 0.10431635344104477, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 78103.94438829373
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__gallbladder_bile]
	mat = database["IT'IS 4.0"]["Bile"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Bile"
		material_settings.MassDensity = 928.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 1.4000000001763189, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 119.99999860058182
	material_settings.ElectricProps.Conductivity = 1.4000000001763189, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 119.99999860058182
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__gallbladder_wall]
	mat = database["IT'IS 4.0"]["Gallbladder"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Gallbladder"
		material_settings.MassDensity = 1070.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.9000471609168963, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 347.4303179117263
	material_settings.ElectricProps.Conductivity = 0.9000471609168963, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 347.4303179117263
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__hypophysis]
	mat = database["IT'IS 4.0"]["Hypophysis"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Hypophysis"
		material_settings.MassDensity = 1053.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.526414671040721, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 28024.231539934775
	material_settings.ElectricProps.Conductivity = 0.526414671040721, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 28024.231539934775
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__eye_vitreous_humor]
	mat = database["IT'IS 4.0"]["Eye (Vitreous Humor)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Eye (Vitreous Humor)"
		material_settings.MassDensity = 1004.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 1.5000000187306728, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 98.97805031949852
	material_settings.ElectricProps.Conductivity = 1.5000000187306728, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 98.97805031949852
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__heart_lumen]
	mat = database["IT'IS 4.0"]["Heart Lumen"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Heart Lumen"
		material_settings.MassDensity = 1049.75, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.7000027557815645, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 5256.784257405785
	material_settings.ElectricProps.Conductivity = 0.7000027557815645, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 5256.784257405785
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__hypothalamus]
	mat = database["IT'IS 4.0"]["Hypothalamus"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Hypothalamus"
		material_settings.MassDensity = 1044.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.10431635344104477, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 78103.94438829373
	material_settings.ElectricProps.Conductivity = 0.10431635344104477, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 78103.94438829373
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__eye_sclera]
	mat = database["IT'IS 4.0"]["Eye (Sclera)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Eye (Sclera)"
		material_settings.MassDensity = 1032.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.5069439115490063, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 28958.108230372378
	material_settings.ElectricProps.Conductivity = 0.5069439115490063, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 28958.108230372378
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__eye_lens]
	mat = database["IT'IS 4.0"]["Eye (Lens)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Eye (Lens)"
		material_settings.MassDensity = 1075.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.20003603389556554, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 974.502773523333
	material_settings.ElectricProps.Conductivity = 0.20003603389556554, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 974.502773523333
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__heart_muscle]
	mat = database["IT'IS 4.0"]["Heart Muscle"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Heart Muscle"
		material_settings.MassDensity = 1080.8, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.12058445748477549, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 214429.83065756533
	material_settings.ElectricProps.Conductivity = 0.12058445748477549, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 214429.83065756533
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__medulla_oblongata]
	mat = database["IT'IS 4.0"]["Medulla Oblongata"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Medulla Oblongata"
		material_settings.MassDensity = 1045.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.12431638861961161, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 78398.8834380823
	material_settings.ElectricProps.Conductivity = 0.12431638861961161, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 78398.8834380823
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__liver]
	mat = database["IT'IS 4.0"]["Liver"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Liver"
		material_settings.MassDensity = 1078.75, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.04390995174029213, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 58022.870650472556
	material_settings.ElectricProps.Conductivity = 0.04390995174029213, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 58022.870650472556
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__larynx]
	mat = database["IT'IS 4.0"]["Larynx"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Larynx"
		material_settings.MassDensity = 1099.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.1751144565321121, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 11324.322841663925
	material_settings.ElectricProps.Conductivity = 0.1751144565321121, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 11324.322841663925
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__intervertebral_disc]
	mat = database["IT'IS 4.0"]["Intervertebral Disc"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Intervertebral Disc"
		material_settings.MassDensity = 1099.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.8300000429213708, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 60.69496869612889
	material_settings.ElectricProps.Conductivity = 0.8300000429213708, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 60.69496869612889
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__lung]
	mat = database["IT'IS 4.0"]["Lung"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Lung"
		material_settings.MassDensity = 394.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.08490129694774125, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 65147.59348631017
	material_settings.ElectricProps.Conductivity = 0.08490129694774125, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 65147.59348631017
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__large_intestine_lumen]
	mat = database["IT'IS 4.0"]["Large Intestine Lumen"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Large Intestine Lumen"
		material_settings.MassDensity = 1045.2, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__kidney_cortex]
	mat = database["IT'IS 4.0"]["Kidney (Cortex)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Kidney (Cortex)"
		material_settings.MassDensity = 1049.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.12049293861089636, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 118267.01561273343
	material_settings.ElectricProps.Conductivity = 0.12049293861089636, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 118267.01561273343
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__large_intestine_wall]
	mat = database["IT'IS 4.0"]["Large Intestine"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Large Intestine"
		material_settings.MassDensity = 1088.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.2362751729236621, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 91734.84188034912
	material_settings.ElectricProps.Conductivity = 0.2362751729236621, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 91734.84188034912
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__lymph_node]
	mat = database["IT'IS 4.0"]["Lymphnode"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Lymphnode"
		material_settings.MassDensity = 1035.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.5900001354811637, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 94.76625288920476
	material_settings.ElectricProps.Conductivity = 0.5900001354811637, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 94.76625288920476
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__kidney_medulla]
	mat = database["IT'IS 4.0"]["Kidney (Medulla)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Kidney (Medulla)"
		material_settings.MassDensity = 1044.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.12049293861089636, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 118267.01561273343
	material_settings.ElectricProps.Conductivity = 0.12049293861089636, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 118267.01561273343
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__mucosa]
	mat = database["IT'IS 4.0"]["Mucous Membrane"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Mucous Membrane"
		material_settings.MassDensity = 1102.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__muscle]
	mat = database["IT'IS 4.0"]["Muscle"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Muscle"
		material_settings.MassDensity = 1090.4, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__meniscus_left, entity__meniscus_right]
	mat = database["IT'IS 4.0"]["Meniscus"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Meniscus"
		material_settings.MassDensity = 1099.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.1751144565321121, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 11324.322841663925
	material_settings.ElectricProps.Conductivity = 0.1751144565321121, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 11324.322841663925
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__nerve]
	mat = database["IT'IS 4.0"]["Nerve"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Nerve"
		material_settings.MassDensity = 1075.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.030580437357960212, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 59931.166247487854
	material_settings.ElectricProps.Conductivity = 0.030580437357960212, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 59931.166247487854
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__pancreas]
	mat = database["IT'IS 4.0"]["Pancreas"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Pancreas"
		material_settings.MassDensity = 1086.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.526414671040721, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 28024.231539934775
	material_settings.ElectricProps.Conductivity = 0.526414671040721, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 28024.231539934775
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__midbrain]
	mat = database["IT'IS 4.0"]["Midbrain"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Midbrain"
		material_settings.MassDensity = 1045.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.12431638861961161, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 78398.8834380823
	material_settings.ElectricProps.Conductivity = 0.12431638861961161, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 78398.8834380823
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__penis]
	mat = database["IT'IS 4.0"]["Penis"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Penis"
		material_settings.MassDensity = 1101.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.3096877839238362, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 40886.44452278335
	material_settings.ElectricProps.Conductivity = 0.3096877839238362, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 40886.44452278335
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__pineal_body]
	mat = database["IT'IS 4.0"]["Pineal Body"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Pineal Body"
		material_settings.MassDensity = 1053.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.526414671040721, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 28024.231539934775
	material_settings.ElectricProps.Conductivity = 0.526414671040721, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 28024.231539934775
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__pons]
	mat = database["IT'IS 4.0"]["Pons"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Pons"
		material_settings.MassDensity = 1045.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.12431638861961161, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 78398.8834380823
	material_settings.ElectricProps.Conductivity = 0.12431638861961161, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 78398.8834380823
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__prostate]
	mat = database["IT'IS 4.0"]["Prostate"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Prostate"
		material_settings.MassDensity = 1045.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.42641623184451083, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 30522.402399893053
	material_settings.ElectricProps.Conductivity = 0.42641623184451083, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 30522.402399893053
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__spinal_cord]
	mat = database["IT'IS 4.0"]["Spinal Cord"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Spinal Cord"
		material_settings.MassDensity = 1075.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.030580437357960212, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 59931.166247487854
	material_settings.ElectricProps.Conductivity = 0.030580437357960212, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 59931.166247487854
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__seminal_vesicle]
	mat = database["IT'IS 4.0"]["Seminal vesicle"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Seminal vesicle"
		material_settings.MassDensity = 1045.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.42641623184451083, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 30522.402399893053
	material_settings.ElectricProps.Conductivity = 0.42641623184451083, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 30522.402399893053
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__tendon_ligament]
	mat = database["IT'IS 4.0"]["Tendon\\Ligament"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Tendon\\Ligament"
		material_settings.MassDensity = 1142.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.3849962787283187, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 54469.261814737656
	material_settings.ElectricProps.Conductivity = 0.3849962787283187, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 54469.261814737656
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__small_intestine_lumen]
	mat = database["IT'IS 4.0"]["Small Intestine Lumen"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Small Intestine Lumen"
		material_settings.MassDensity = 1045.2, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__spleen]
	mat = database["IT'IS 4.0"]["Spleen"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Spleen"
		material_settings.MassDensity = 1089.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.10592230313420366, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 43607.03551376055
	material_settings.ElectricProps.Conductivity = 0.10592230313420366, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 43607.03551376055
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__salivary_gland]
	mat = database["IT'IS 4.0"]["Salivary Gland"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Salivary Gland"
		material_settings.MassDensity = 1048.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.6700001297062389, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 91.54998558977785
	material_settings.ElectricProps.Conductivity = 0.6700001297062389, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 91.54998558977785
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity_sat]
	mat = database["IT'IS 4.0"]["SAT (Subcutaneous Fat)"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "SAT (Subcutaneous Fat)"
		material_settings.MassDensity = 911.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.04242149292939708, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 6425.317623083546
	material_settings.ElectricProps.Conductivity = 0.04242149292939708, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 6425.317623083546
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__small_intestine_wall]
	mat = database["IT'IS 4.0"]["Small Intestine"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Small Intestine"
		material_settings.MassDensity = 1030.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.5430583270731406, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 134821.86879949042
	material_settings.ElectricProps.Conductivity = 0.5430583270731406, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 134821.86879949042
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__stomach_lumen]
	mat = database["IT'IS 4.0"]["Stomach Lumen"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Stomach Lumen"
		material_settings.MassDensity = 1045.2, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	material_settings.ElectricProps.Conductivity = 0.33158456993102237, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 124369.71734477596
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__stomach_wall]
	mat = database["IT'IS 4.0"]["Stomach"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Stomach"
		material_settings.MassDensity = 1088.0, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.5264137798165603, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 27530.286281412
	material_settings.ElectricProps.Conductivity = 0.5264137798165603, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 27530.286281412
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__ureter, entity__urethra]
	mat = database["IT'IS 4.0"]["Ureter\\Urethra"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Ureter\\Urethra"
		material_settings.MassDensity = 1101.5, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.3096877839238362, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 40886.44452278335
	material_settings.ElectricProps.Conductivity = 0.3096877839238362, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 40886.44452278335
	simulation.Add(material_settings, components)

	# Adding a new MaterialSettings
	material_settings = emlf.MaterialSettings()
	components = [entity__tongue]
	mat = database["IT'IS 4.0"]["Tongue"]
	if mat is not None:
		simulation.LinkMaterialWithDatabase(material_settings, mat)
	else:
		# Fallback if material is not found
		material_settings.Name = "Tongue"
		material_settings.MassDensity = 1090.4, Unit("kg/m^3")
		material_settings.ElectricProps.Conductivity = 0.2764156075225741, Unit("S/m")
		material_settings.ElectricProps.RelativePermittivity = 29518.134056388964
	material_settings.ElectricProps.Conductivity = 0.2764156075225741, Unit("S/m")
	material_settings.ElectricProps.RelativePermittivity = 29518.134056388964
	simulation.Add(material_settings, components)

	# Adding a new CurrentSourceSettings
	current_source_settings = emlf.CurrentSourceSettings()
	components = [entity_lf1, entity_lf1_1, entity_lf2, entity_lf3, entity_lf4_1, entity_lf5, entity_lf6, entity_lf7, entity_lf8_1]
	current_source_settings.Amplitude = -5000.0, units.Amperes
	simulation.Add(current_source_settings, components)

	# Adding a new CurrentSourceSettings
	current_source_settings = emlf.CurrentSourceSettings()
	components = [entity_lf1_2, entity_lf2_1, entity_lf3_1, entity_lf4, entity_lf5_1, entity_lf6_1, entity_lf7_1, entity_lf8, entity_lf9]
	current_source_settings.Name = "Wire Current Settings 1"
	current_source_settings.Amplitude = 5000.0, units.Amperes
	simulation.Add(current_source_settings, components)

	# Editing GlobalGridSettings "Grid (Empty)"
	global_grid_settings = simulation.GlobalGridSettings
	global_grid_settings.DiscretizationMode = global_grid_settings.DiscretizationMode.enum.Manual
	global_grid_settings.Resolution = numpy.array([3.0, 3.0, 3.0]), units.MilliMeters
	global_grid_settings.PaddingMode = global_grid_settings.PaddingMode.enum.Manual
	global_grid_settings.BottomPadding = numpy.array([70.0, 110.0, 50.0]), units.MilliMeters
	global_grid_settings.TopPadding = numpy.array([70.0, 160.0, 10.0]), units.MilliMeters

	# Editing AutomaticGridSettings "Automatic"
	automatic_grid_settings = [x for x in simulation.AllSettings if isinstance(x, emlf.AutomaticGridSettings) and x.Name == "Automatic"][0]
	components = [entity_angled_bilateral_conductive, entity_angled_bilateral_insulation]
	simulation.Add(automatic_grid_settings, components)

	# Adding a new ManualGridSettings
	manual_grid_settings = simulation.AddManualGridSettings([entity_lf1, entity_lf1_1, entity_lf1_2, entity_lf2, entity_lf2_1, entity_lf3, entity_lf3_1, entity_lf4, entity_lf4_1, entity_lf5, entity_lf5_1, entity_lf6, entity_lf6_1, entity_lf7, entity_lf7_1, entity_lf8, entity_lf8_1, entity_lf9])
	manual_grid_settings.Resolution = numpy.array([3.0, 3.0, 3.0]), units.MilliMeters

	# Editing AutomaticVoxelerSettings "Automatic Voxeler Settings"
	automatic_voxeler_settings = [x for x in simulation.AllSettings if isinstance(x, emlf.AutomaticVoxelerSettings) and x.Name == "Automatic Voxeler Settings"][0]
	components = [entity_angled_bilateral_conductive, entity_angled_bilateral_insulation, entity_lf1, entity_lf1_1, entity_lf1_2, entity_lf2, entity_lf2_1, entity_lf3, entity_lf3_1, entity_lf4, entity_lf4_1, entity_lf5, entity_lf5_1, entity_lf6, entity_lf6_1, entity_lf7, entity_lf7_1, entity_lf8, entity_lf8_1, entity_lf9]
	simulation.Add(automatic_voxeler_settings, components)

	# Adding a new AutomaticVoxelerSettings
	automatic_voxeler_settings = emlf.AutomaticVoxelerSettings()
	components = [entity__adrenal_gland, entity__air_internal, entity__artery, entity__bladder_wall, entity__bronchus_lumen, entity__bronchus_wall, entity__carpalia__metacarpalia_cancellous_left, entity__carpalia__metacarpalia_cancellous_right, entity__carpalia__metacarpalia_cortical_left, entity__carpalia__metacarpalia_cortical_right, entity__cartilage, entity__cerebellum, entity__cerebrospinal_fluid, entity__cerebrum_grey_matter, entity__cerebrum_white_matter, entity__commissura_anterior, entity__commissura_posterior, entity__corpus_callosum, entity__diaphragm, entity__ductus_deferens, entity__dura_mater, entity__ear_cartilage_left, entity__ear_cartilage_right, entity__ear_skin_left, entity__ear_skin_right, entity__epididymis, entity__esophagus_lumen, entity__esophagus_wall, entity__eye_cornea, entity__eye_lens, entity__eye_sclera, entity__eye_vitreous_humor, entity__fat, entity__femur_cancellous_left, entity__femur_cancellous_right, entity__femur_cortical_left, entity__femur_cortical_right, entity__femur_yellow_marrow_left, entity__femur_yellow_marrow_right, entity__fibula_cancellous_left, entity__fibula_cancellous_right, entity__fibula_cortical_left, entity__fibula_cortical_right, entity__fibula_yellow_marrow_left, entity__fibula_yellow_marrow_right, entity__foot_cancellous_left, entity__foot_cancellous_right, entity__foot_cortical_left, entity__foot_cortical_right, entity__gallbladder_bile, entity__gallbladder_wall, entity__heart_lumen, entity__heart_muscle, entity__hippocampus, entity__humerus_cancellous_left, entity__humerus_cancellous_right, entity__humerus_cortical_left, entity__humerus_cortical_right, entity__humerus_yellow_marrow_left, entity__humerus_yellow_marrow_right, entity__hyoid_cancellous, entity__hyoid_cortical, entity__hypophysis, entity__hypothalamus, entity__intervertebral_disc, entity__kidney_cortex, entity__kidney_medulla, entity__large_intestine_lumen, entity__large_intestine_wall, entity__larynx, entity__liver, entity__lung, entity__lymph_node, entity__mandible_cancellous, entity__mandible_cortical, entity__medulla_oblongata, entity__meniscus_left, entity__meniscus_right, entity__metacarpus_i_cancellous_left, entity__metacarpus_i_cancellous_right, entity__metacarpus_i_cortical_left, entity__metacarpus_i_cortical_right, entity__midbrain, entity__mucosa, entity__muscle, entity__nerve, entity__pancreas, entity__patella_cancellous_left, entity__patella_cancellous_right, entity__patella_cortical_left, entity__patella_cortical_right, entity__pelvis_cancellous, entity__pelvis_cortical, entity__penis, entity__phalanx_distalis_i_cancellous_left, entity__phalanx_distalis_i_cancellous_right, entity__phalanx_distalis_i_cortical_left, entity__phalanx_distalis_i_cortical_right, entity__phalanx_distalis_ii_cancellous_left, entity__phalanx_distalis_ii_cancellous_right, entity__phalanx_distalis_ii_cortical_left, entity__phalanx_distalis_ii_cortical_right, entity__phalanx_distalis_iii_cancellous_left, entity__phalanx_distalis_iii_cancellous_right, entity__phalanx_distalis_iii_cortical_left, entity__phalanx_distalis_iii_cortical_right, entity__phalanx_distalis_iv_cancellous_left, entity__phalanx_distalis_iv_cancellous_right, entity__phalanx_distalis_iv_cortical_left, entity__phalanx_distalis_iv_cortical_right, entity__phalanx_distalis_v_cancellous_left, entity__phalanx_distalis_v_cancellous_right, entity__phalanx_distalis_v_cortical_left, entity__phalanx_distalis_v_cortical_right, entity__phalanx_media_ii_cancellous_left, entity__phalanx_media_ii_cancellous_right, entity__phalanx_media_ii_cortical_left, entity__phalanx_media_ii_cortical_right, entity__phalanx_media_iii_cancellous_left, entity__phalanx_media_iii_cancellous_right, entity__phalanx_media_iii_cortical_left, entity__phalanx_media_iii_cortical_right, entity__phalanx_media_iv_cancellous_left, entity__phalanx_media_iv_cancellous_right, entity__phalanx_media_iv_cortical_left, entity__phalanx_media_iv_cortical_right, entity__phalanx_media_v_cancellous_left, entity__phalanx_media_v_cancellous_right, entity__phalanx_media_v_cortical_left, entity__phalanx_media_v_cortical_right, entity__phalanx_proximalis_i_cancellous_left, entity__phalanx_proximalis_i_cancellous_right, entity__phalanx_proximalis_i_cortical_left, entity__phalanx_proximalis_i_cortical_right, entity__phalanx_proximalis_ii_cancellous_left, entity__phalanx_proximalis_ii_cancellous_right, entity__phalanx_proximalis_ii_cortical_left, entity__phalanx_proximalis_ii_cortical_right, entity__phalanx_proximalis_iii_cancellous_left, entity__phalanx_proximalis_iii_cancellous_right, entity__phalanx_proximalis_iii_cortical_left, entity__phalanx_proximalis_iii_cortical_right, entity__phalanx_proximalis_iv_cancellous_left, entity__phalanx_proximalis_iv_cancellous_right, entity__phalanx_proximalis_iv_cortical_left, entity__phalanx_proximalis_iv_cortical_right, entity__phalanx_proximalis_v_cancellous_left, entity__phalanx_proximalis_v_cancellous_right, entity__phalanx_proximalis_v_cortical_left, entity__phalanx_proximalis_v_cortical_right, entity__pineal_body, entity__pons, entity__prostate, entity__radius_cancellous_left, entity__radius_cancellous_right, entity__radius_cortical_left, entity__radius_cortical_right, entity__radius_yellow_marrow_left, entity__radius_yellow_marrow_right, entity__salivary_gland, entity__seminal_vesicle, entity__skin, entity__skull_cancellous, entity__skull_cortical, entity__small_intestine_lumen, entity__small_intestine_wall, entity__spinal_cord, entity__spleen, entity__stomach_lumen, entity__stomach_wall, entity__tendon_ligament, entity__testis, entity__thalamus, entity__thorax_cancellous, entity__thorax_cortical, entity__thyroid_gland, entity__tibia_cancellous_left, entity__tibia_cancellous_right, entity__tibia_cortical_left, entity__tibia_cortical_right, entity__tibia_yellow_marrow_left, entity__tibia_yellow_marrow_right, entity__tongue, entity__tooth, entity__trachea_lumen, entity__trachea_wall, entity__ulna_cancellous_left, entity__ulna_cancellous_right, entity__ulna_cortical_left, entity__ulna_cortical_right, entity__ulna_yellow_marrow_left, entity__ulna_yellow_marrow_right, entity__ureter, entity__urethra, entity__urine, entity__vein, entity__vertebra_cancellous_c1, entity__vertebra_cancellous_c2, entity__vertebra_cancellous_c3, entity__vertebra_cancellous_c4, entity__vertebra_cancellous_c5, entity__vertebra_cancellous_c6, entity__vertebra_cancellous_c7, entity__vertebra_cancellous_l1, entity__vertebra_cancellous_l2, entity__vertebra_cancellous_l3, entity__vertebra_cancellous_l4, entity__vertebra_cancellous_l5, entity__vertebra_cancellous_os_sacrum_coccyx, entity__vertebra_cancellous_t1, entity__vertebra_cancellous_t10, entity__vertebra_cancellous_t11, entity__vertebra_cancellous_t12, entity__vertebra_cancellous_t2, entity__vertebra_cancellous_t3, entity__vertebra_cancellous_t4, entity__vertebra_cancellous_t5, entity__vertebra_cancellous_t6, entity__vertebra_cancellous_t7, entity__vertebra_cancellous_t8, entity__vertebra_cancellous_t9, entity__vertebra_cortical_c1, entity__vertebra_cortical_c2, entity__vertebra_cortical_c3, entity__vertebra_cortical_c4, entity__vertebra_cortical_c5, entity__vertebra_cortical_c6, entity__vertebra_cortical_c7, entity__vertebra_cortical_l1, entity__vertebra_cortical_l2, entity__vertebra_cortical_l3, entity__vertebra_cortical_l4, entity__vertebra_cortical_l5, entity__vertebra_cortical_os_sacrum_coccyx, entity__vertebra_cortical_t1, entity__vertebra_cortical_t10, entity__vertebra_cortical_t11, entity__vertebra_cortical_t12, entity__vertebra_cortical_t2, entity__vertebra_cortical_t3, entity__vertebra_cortical_t4, entity__vertebra_cortical_t5, entity__vertebra_cortical_t6, entity__vertebra_cortical_t7, entity__vertebra_cortical_t8, entity__vertebra_cortical_t9, entity_sat]
	automatic_voxeler_settings.Name = "DUKE_POSABLE 3.0 Voxels"
	simulation.Add(automatic_voxeler_settings, components)

	# Update the materials with the new frequency parameters
	simulation.UpdateAllMaterials()

	# Update the grid with the new parameters
	simulation.UpdateGrid()

	# Add the simulation to the UI
	document.AllSimulations.Add( simulation )
except Exception as exc:
	import traceback
	traceback.print_exc(exc)
	# Reset active version to default
	ReleaseVersion.reset()
	raise(exc)