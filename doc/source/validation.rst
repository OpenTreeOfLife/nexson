********************************************************
:mod:`nexson.validation`: Validation of NexSON documents
********************************************************


.. highlight:: python
.. code-block:: python

        obj = json.load(inp)
        v_log, adaptor = validate_nexson(obj)
        annotation = v_log.prepare_annotation(author_name=SCRIPT_NAME,
                                              invocation=sys.argv[1:],
                                              )
        adaptor.add_or_replace_annotation(obj,
                                          annotation['annotationEvent'],
                                          annotation['agent'],
                                          add_agent_only=args.add_agent_only)

Validation
==========

.. autofunction:: nexson.validation.validate_nexson
.. autofunction:: nexson.validation.ot_validate
