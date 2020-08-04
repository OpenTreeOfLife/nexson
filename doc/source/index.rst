***************************************
:mod:`nexson`: Tools for NexSON formats
***************************************

.. toctree::
    :maxdepth: 3
    :hidden:

    Overview <self>
    validation.rst
    validation-loggers.rst

.. automodule:: nexson

The package is organized into subpackages for ease of maintenance.
However, the public functions are imported into `nexson.__init__.py`,
so users can ignore the subpackage structure.


See https://opentreeoflife.github.io/ for general information about the
Open Tree of Life project.

Validation
==========

.. toctree::
    :maxdepth: 2

    validation.rst
    validation-logger.rst



.. autofunction:: add_literal_meta
.. autofunction:: add_resource_meta
.. autofunction:: add_schema_attributes
.. autofunction:: BADGER_FISH_NEXSON_VERSION
.. autofunction:: BY_ID_HONEY_BADGERFISH
.. autofunction:: can_convert_nexson_forms
.. autofunction:: check_raw_dict
.. autofunction:: ConversionConfig
.. autofunction:: convert_nexson_format
.. autofunction:: create_content_spec
.. autofunction:: create_validation_adaptor
.. autofunction:: DEFAULT_NEXSON_VERSION,
.. autofunction:: delete_first_literal_meta
.. autofunction:: detect_nexson_version
.. autofunction:: DIRECT_HONEY_BADGERFISH
.. autofunction:: errorReturn
.. autofunction:: extract_meta
.. autofunction:: extract_supporting_file_messages
.. autofunction:: extract_tree
.. autofunction:: extract_tree_nexson
.. autofunction:: find_nested_meta_first
.. autofunction:: find_val_literal_meta_first
.. autofunction:: get_empty_nexson
.. autofunction:: get_nexml_el
.. autofunction:: get_ot_study_info_from_nexml
.. autofunction:: import_nexson_from_treebase
.. autofunction:: merge_otus_and_trees
.. autofunction:: NEXML_NEXSON_VERSION,
.. autofunction:: NexsonConverter
.. autofunction:: NexsonError
.. autofunction:: NexsonWarningCodes

.. autofunction:: PhyloSchema
.. autofunction:: SeverityCodes
.. autofunction:: sort_arbitrarily_ordered_nexson
.. autofunction:: sort_meta_elements
.. autofunction:: SUPPORTED_NEXSON_VERSIONS
.. autofunction:: write_obj_as_nexml


.. autofunction:: _add_uniq_value_to_dict_bf
.. autofunction:: _add_value_to_dict_bf
.. autofunction:: _coerce_literal_val_to_primitive,
.. autofunction:: _cull_redundant_about,
.. autofunction:: _get_index_list_of_values
.. autofunction:: _index_list_of_values
.. autofunction:: _is_badgerfish_version
.. autofunction:: _is_by_id_hbf
.. autofunction:: _is_direct_hbf
.. autofunction:: _is_supported_nexson_vers
.. autofunction:: _LITERAL_META_PAT
.. autofunction:: _NEXEL
.. autofunction:: _RESOURCE_META_PAT
.. autofunction:: _simplify_all_meta_by_id_del