#include "%SERVICE_NAME_PASCAL%.h"
#include "ErrorNo.h"

%SERVICE_NAME_PASCAL%::%SERVICE_NAME_PASCAL%(MicroBitPeridoRadio& r) : radio(r)
{
    %SERVICE_CONSTRUCTOR_BODY%
}

void %SERVICE_NAME_PASCAL%::idleTick()
{
    %SERVICE_IDLE_BODY%
}

%SERVICE_MEMBER_FUNCTION_IMPLEMENTATIONS%