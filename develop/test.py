from pycalphad.core.calculate import calculate
from pycalphad.io.database import Database
from pycalphad.core.utils import instantiate_models

db_alzn = Database('cfe_broshe.tdb') #''..//cfe_broshe.tdb alzn_mey.tdb

#my_phases_alzn = ['LIQUID', 'FCC_A1', 'HCP_A3']
models = instantiate_models(db_alzn, ['Fe', 'C', 'VA'], ['LIQUID'], model=None, parameters=dict())
a = calculate(db_alzn, ['Fe', 'C', 'VA'], ['LIQUID'])
#a = calculate.calculate()

from pycalphad.core.utils import endmember_matrix