********************************************************
:mod:`nexson.validation`: Validation of NexSON documents
********************************************************

The validation of a NexSON object is a bit more cumbersome than
it should be. In part, this is because the system to separate
the accumulation of warnings/errors in one container, and also
allowing for attaching messages about these errors to the NexSON
object. Thus, the `validate_nexson` function returns a pair of
objects: a log and an adaptor that can inject the logged messages
into the correct spot in the NexSON.

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
