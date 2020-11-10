from pipeline.conf import settings
from pipeline.compressors import SubProcessCompressor


class TerserCompressor(SubProcessCompressor):
    def compress_js(self, js):
        command = (settings.TERSER_BINARY, settings.TERSER_ARGUMENTS)
        return self.execute_command(command, js)
