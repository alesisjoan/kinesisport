# -*- coding: utf-8 -*-
import sys
if sys.version_info > (3, 0):
    from . import afiliacion
    from . import revisacion
    from . import estudio
    from . import partner
    from . import actividad
    from . import plan
else:
    import afiliacion
    import revisacion
    import estudio
    import partner
    import actividad
    import plan
