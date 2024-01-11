import grpc
import time
import contextvars

import typing as T

token_cvar = contextvars.ContextVar("token_cvar", default="default")


class AuthenJwtInterceptor(grpc.aio.ServerInterceptor):  # type: ignore

    async def intercept_service(
        self,
        continuation: T.Callable[
            ["grpc.HandlerCallDetails"], T.Optional["T.Awaitable[grpc.RpcMethodHandler[T.Any, T.Any]]"]
        ],
        handler_call_details: "grpc.HandlerCallDetails",
    ) -> "grpc.RpcMethodHandler[T.Any, T.Any]":
        
        token = self.extract_token(handler_call_details.invocation_metadata)

        token_cvar.set(f"{token}-uuid-{time.time()}")
        handler = continuation(handler_call_details)
        assert handler is not None
        return await handler
     
    def extract_token(self, metadata: "grpc.Metadata") -> T.Optional[str]:
        for k, v in metadata:
            if k != "authorization" or not v:
                continue
            return str(v)
        return None
