__version__ = '3.1.1'

# required for Python 3.8 on Windows
import os
if hasattr(os, 'add_dll_directory'):
    if os.getenv('SCIPOPTDIR'):
        os.add_dll_directory(os.path.join(os.getenv('SCIPOPTDIR').strip('"'), 'bin'))

# export user-relevant objects:
from .Multidict import multidict
from .scip      import Model
from .scip      import Benders
from .scip      import Benderscut
from .scip      import Branchrule
from .scip      import Nodesel
from .scip      import Conshdlr
from .scip      import Eventhdlr
from .scip      import Heur
from .scip      import Presol
from .scip      import Pricer
from .scip      import Prop
from .scip      import Sepa
from .scip      import LP
from .scip      import Expr
from .scip      import quicksum
from .scip      import quickprod
from .scip      import exp
from .scip      import log
from .scip      import sqrt
from .scip      import PY_SCIP_RESULT       as SCIP_RESULT
from .scip      import PY_SCIP_PARAMSETTING as SCIP_PARAMSETTING
from .scip      import PY_SCIP_PARAMEMPHASIS as SCIP_PARAMEMPHASIS
from .scip      import PY_SCIP_STATUS       as SCIP_STATUS
from .scip      import PY_SCIP_STAGE        as SCIP_STAGE
from .scip      import PY_SCIP_PROPTIMING   as SCIP_PROPTIMING
from .scip      import PY_SCIP_PRESOLTIMING as SCIP_PRESOLTIMING
from .scip      import PY_SCIP_HEURTIMING   as SCIP_HEURTIMING
from .scip      import PY_SCIP_EVENTTYPE    as SCIP_EVENTTYPE
from .scip      import PY_SCIP_LPSOLSTAT    as SCIP_LPSOLSTAT
from .scip      import PY_SCIP_BRANCHDIR    as SCIP_BRANCHDIR
from .scip      import PY_SCIP_BENDERSENFOTYPE as SCIP_BENDERSENFOTYPE
from .scip      import PY_SCIP_ROWORIGINTYPE as SCIP_ROWORIGINTYPE
