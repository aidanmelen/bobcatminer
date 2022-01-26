from typing import List

try:
    from api import BobcatAPI
except:
    from .api import BobcatAPI

try:
    from logger import BobcatLogger
except:
    from .logger import BobcatLogger


class Bobcat(BobcatAPI):
    """A class for the Bobcat miner."""

    def __init__(
        self,
        hostname: str = None,
        animal: str = None,
        networks: List[str] = ["192.168.0.0/24", "10.0.0.0/24"],
        dry_run: bool = False,
        log_file: str = None,
        discord_webhook_url: str = None,
        log_level: str = "DEBUG",
        log_level_stream: str = "INFO",
        log_level_file: str = "DEBUG",
        log_level_discord: str = "WARN",
    ) -> None:

        bobcat_logger = BobcatLogger(
            log_file=log_file,
            discord_webhook_url=discord_webhook_url,
            log_level=log_level,
            log_level_stream=log_level_stream,
            log_level_file=log_level_file,
            log_level_discord=log_level_discord,
        )

        super().__init__(hostname, animal, networks, dry_run, bobcat_logger.logger)

    @property
    def status(self):
        """Get status."""
        if not self.status_data:
            self.refresh_status()
        return self.status_data.get("status")

    @property
    def gap(self):
        """Get gap."""
        if not self.status_data:
            self.refresh_status()
        gap = self.status_data.get("gap")
        return int(gap) if gap.lstrip("-").isdigit() else gap

    @property
    def blockchain_height(self):
        """Get blockchain height."""
        if not self.status_data:
            self.refresh_status()
        blockchain_height = self.status_data.get("blockchain_height")
        return (
            int(blockchain_height) if blockchain_height.lstrip("-").isdigit() else blockchain_height
        )

    @property
    def epoch(self):
        """Get epoch."""
        if not self.status_data:
            self.refresh_status()
        epoch = self.status_data.get("epoch")
        return int(epoch) if epoch.lstrip("-").isdigit() else epoch

    @property
    def tip(self):
        """Get tip. Only available during error state."""
        if not self.status_data:
            self.refresh_status()
        return self.status_data.get("tip")

    @property
    def ota_version(self):
        """Get OTA version."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("ota_version")

    @property
    def region(self):
        """Get region."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("region")

    @property
    def frequency_plan(self):
        """Get frequency plan."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("frequency_plan")

    @property
    def animal(self):
        """Get animal."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("animal")

    @property
    def name(self):
        """Get human readable name."""
        return " ".join([word.capitalize() for word in self.animal.split("-")])

    @property
    def pubkey(self):
        """Get pubic key."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("pubkey")

    @property
    def state(self):
        """Get miner state."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("miner", {}).get("State")

    @property
    def miner_status(self):
        """Get miner status."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("miner", {}).get("Status")

    @property
    def miner_height(self):
        """Get miner height."""
        if not self.status_data:
            self.refresh_status()
        miner_height = self.status_data.get("miner_height")
        return int(miner_height) if miner_height.lstrip("-").isdigit() else miner_height

    @property
    def miner_alert(self):
        """Get miner status."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("miner_alert", {})

    @property
    def miner_desc(self):
        """Get miner status."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("miner_desc", {})

    @property
    def names(self):
        """Get miner names."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("miner", {}).get("Names")

    @property
    def image(self):
        """Get miner image."""
        # https://bobcatminer.zendesk.com/hc/en-us/articles/4413004080667-Access-Diagnoser-Check-OTA-Version
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("miner", {}).get("Image")

    @property
    def created(self):
        """Get miner created."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("miner", {}).get("Created")

    @property
    def p2p_status(self):
        """Get p2p status."""
        if not self.miner_data:
            self.refresh_miner()
        return "\n".join(self.miner_data.get("p2p_status"))

    @property
    def ports_desc(self):
        """Get port description."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("ports_desc")

    @property
    def ports(self):
        """Get ports."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("ports", {})

    @property
    def private_ip(self):
        """Get private ip."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("private_ip")

    @property
    def public_ip(self):
        """Get public ip."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("public_ip")

    @property
    def peerbook(self):
        """Get peerbook."""
        if not self.miner_data:
            self.refresh_miner()
        return "\n".join(self.miner_data.get("peerbook", []))

    @property
    def timestamp(self):
        """Get timestamp."""
        if not self.miner_data:
            self.refresh_miner()
        return self.miner_data.get("timestamp")

    @property
    def error(self):
        """Get error."""
        if not self.miner_data:
            self.refresh_miner()

        _err = self.miner_data.get("error")

        return _err if _err else None

    @property
    def temp0(self):
        """Get CPU temp sensor 0 Celsius."""
        if not self.temp_data:
            self.refresh_temp()
        return int(self.temp_data.get("temp0"))

    @property
    def temp1(self):
        """Get CPU temp sensor 1 in Celsius."""
        if not self.temp_data:
            self.refresh_temp()
        return int(self.temp_data.get("temp1"))

    @property
    def highest_temp(self):
        """Get the highest of the CPU temp from the two sensor."""
        return self.temp0 if self.temp0 > self.temp1 else self.temp1

    @property
    def temp0_c(self):
        """Get CPU temp sensor 0 in Celsius."""
        return self.temp0

    @property
    def temp1_c(self):
        """Get CPU temp sensor 1 in Celsius."""
        return self.temp1

    @property
    def temp0_f(self):
        """Get CPU temp sensor 0 Fahrenheit."""
        return round(self.temp0 * 1.8 + 32, 1)

    @property
    def temp1_f(self):
        """Get CPU temp sensor 1 in Fahrenheit."""
        return round(self.temp1 * 1.8 + 32, 1)

    @property
    def download_speed(self):
        """Get download speed."""
        if not self.speed_data:
            self.refresh_speed()
        return self.speed_data.get("DownloadSpeed")

    @property
    def upload_speed(self):
        """Get upload speed."""
        if not self.speed_data:
            self.refresh_speed()
        return self.speed_data.get("UploadSpeed")

    @property
    def latency(self):
        """Get latency."""
        if not self.speed_data:
            self.refresh_speed()
        return self.speed_data.get("Latency")

    @property
    def dig_name(self):
        """Get dig name."""
        if not self.dig_data:
            self.refresh_dig()
        return self.dig_data.get("name")

    @property
    def dig_message(self):
        """Get dig message."""
        if not self.dig_data:
            self.refresh_dig()
        return self.dig_data.get("message")

    @property
    def dig_dns(self):
        """Get dig DNS."""
        if not self.dig_data:
            self.refresh_dig()
        return self.dig_data.get("DNS")

    @property
    def dig_records(self):
        """Get dig records."""
        if not self.dig_data:
            self.refresh_dig()
        return self.dig_data.get("records", [])
