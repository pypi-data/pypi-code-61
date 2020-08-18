from typing import BinaryIO

from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync
from neuroio.constants import EntryResult
from neuroio.utils import request_dict_processing


class Persons(APIBase):
    def create(
        self,
        image: BinaryIO,
        source: str,
        facesize: int,
        create_on_ha: bool,
        create_on_junk: bool,
        identify_asm: bool,
    ) -> Response:
        files = {"image": image}
        data = {
            "source": source,
            "facesize": str(facesize),
            "create_on_ha": str(create_on_ha),
            "create_on_junk": str(create_on_junk),
            "identify_asm": str(identify_asm),
        }
        try:
            return self.client.post(url="/v1/persons/", data=data, files=files)
        finally:
            self.client.close()

    def create_by_entry(
        self, id: int, create_on_ha: bool, create_on_junk: bool
    ) -> Response:
        data = request_dict_processing(locals(), ["self"])

        try:
            return self.client.post(url="/v1/persons/entry/", json=data)
        finally:
            self.client.close()

    def reinit(self, id: int) -> Response:
        try:
            return self.client.post(url="/v1/persons/reinit/", json={"id": id})
        finally:
            self.client.close()

    def reinit_by_photo(
        self,
        pid: str,
        image: BinaryIO,
        source: str,
        facesize: int,
        identify_asm: bool,
        result: str = EntryResult.HA,
    ) -> Response:
        files = {"image": image}
        data = {
            "source": source,
            "facesize": str(facesize),
            "identify_asm": str(identify_asm),
            "result": result,
        }

        try:
            return self.client.post(
                url=f"/v1/persons/reinit/{pid}/", data=data, files=files
            )
        finally:
            self.client.close()

    def search(self, image: BinaryIO, identify_asm: bool = False) -> Response:
        files = {"image": ("image", image, "image/jpeg")}
        data = {"identify_asm": str(identify_asm)}
        try:
            return self.client.post(
                url="/v1/persons/search/", data=data, files=files
            )
        finally:
            self.client.close()

    def delete(self, pid: str) -> Response:
        try:
            return self.client.delete(url=f"/v1/persons/{pid}/")
        finally:
            self.client.close()


class PersonsAsync(APIBaseAsync):
    async def create(
        self,
        image: BinaryIO,
        source: str,
        facesize: int,
        create_on_ha: bool,
        create_on_junk: bool,
        identify_asm: bool,
    ) -> Response:
        files = {"image": image}
        data = {
            "source": source,
            "facesize": str(facesize),
            "create_on_ha": str(create_on_ha),
            "create_on_junk": str(create_on_junk),
            "identify_asm": str(identify_asm),
        }
        try:
            return await self.client.post(
                url="/v1/persons/", data=data, files=files
            )
        finally:
            await self.client.aclose()

    async def create_by_entry(
        self, id: int, create_on_ha: bool, create_on_junk: bool
    ) -> Response:
        data = request_dict_processing(locals(), ["self"])

        try:
            return await self.client.post(url="/v1/persons/entry/", json=data)
        finally:
            await self.client.aclose()

    async def reinit(self, id: int) -> Response:
        try:
            return await self.client.post(
                url="/v1/persons/reinit/", json={"id": id}
            )
        finally:
            await self.client.aclose()

    async def reinit_by_photo(
        self,
        pid: str,
        image: BinaryIO,
        source: str,
        facesize: int,
        identify_asm: bool,
        result: str = EntryResult.HA,
    ) -> Response:
        files = {"image": image}
        data = {
            "source": source,
            "facesize": str(facesize),
            "identify_asm": str(identify_asm),
            "result": result,
        }

        try:
            return await self.client.post(
                url=f"/v1/persons/reinit/{pid}/", data=data, files=files
            )
        finally:
            await self.client.aclose()

    async def search(
        self, image: BinaryIO, identify_asm: bool = False
    ) -> Response:
        files = {"image": ("image", image, "image/jpeg")}
        data = {"identify_asm": str(identify_asm)}
        try:
            return await self.client.post(
                url="/v1/persons/search/", data=data, files=files
            )
        finally:
            await self.client.aclose()

    async def delete(self, pid: str) -> Response:
        try:
            return await self.client.delete(url=f"/v1/persons/{pid}/")
        finally:
            await self.client.aclose()
