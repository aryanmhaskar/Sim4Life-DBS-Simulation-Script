# -*- coding: utf-8 -*-

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
	# Implementation not shown (several lines of defining variables)

	# Editing QuasiStaticSetupSettings "Setup"
	quasi_static_setup_settings = [x for x in simulation.AllSettings if isinstance(x, emlf.QuasiStaticSetupSettings) and x.Name == "Setup"][0]
	quasi_static_setup_settings.Frequency = 2500.0, units.Hz

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