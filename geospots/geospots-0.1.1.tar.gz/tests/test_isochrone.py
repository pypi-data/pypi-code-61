from geospots.isochrones import return_iso

a=return_iso( 
    api_key='5b3ce3597851110001cf62488b98dba3f6c7452b9d391c8306afa037',
    locations=[[-48.51057, -27.57482]],
    range=[5]
)

print(a)