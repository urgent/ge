import great_expectations as ge

# Load the Data Context
context = ge.data_context.DataContext()

# The batch_kwargs will differ depending on the type of Datasource,
# see the docs for help
batch_kwargs = {'table': 'campaigns',
                'datasource': 'campaign', "result_format": "COMPLETE"}
batch = context.get_batch(batch_kwargs, 'campaigns.warning')

# Run validation on your Batch
results = context.run_validation_operator(
    "action_list_operator",
    assets_to_validate=[batch],
    run_id='my_run_id')

test2 = results.items()


rows = results.list_validation_results()
for row in rows[0].results:
    if(not row.success):
        test = row.result
        print('test')
