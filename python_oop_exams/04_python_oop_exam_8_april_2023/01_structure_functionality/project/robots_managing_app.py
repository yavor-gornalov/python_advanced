from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")

        new_service = self.SERVICE_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        new_robot = self.ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._get_robot_by_name(robot_name)
        service = self._get_service_by_name(service_name)
        result = self._check_robot__and_service_types_consistency(robot, service)
        if result:
            return result
        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._get_service_by_name(service_name)
        robot = self._get_robot_from_service(robot_name, service)
        if robot is None:
            raise Exception("No such robot in this service!")
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self._get_service_by_name(service_name)
        number_of_robots_fed = len([r.eating() for r in service.robots])
        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = self._get_service_by_name(service_name)
        total_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        [result.append(service.details()) for service in self.services]
        return "\n".join(result)

    # HELPERS
    def _get_robot_by_name(self, robot_name):
        collection = [r for r in self.robots if r.name == robot_name]
        return collection[0] if collection else None

    @staticmethod
    def _get_robot_from_service(robot_name, service: BaseService):
        collection = [r for r in service.robots if r.name == robot_name]
        return collection[0] if collection else None

    def _get_service_by_name(self, service_name):
        collection = [s for s in self.services if s.name == service_name]
        return collection[0] if collection else None

    @staticmethod
    def _check_robot__and_service_types_consistency(robot: BaseRobot, service: BaseService):
        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "SecondaryService":
            return
        if robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "MainService":
            return
        return "Unsuitable service."
