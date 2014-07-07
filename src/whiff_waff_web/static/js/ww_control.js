//http://stackoverflow.com/questions/18461263/can-an-angularjs-controller-inherit-from-another-contoller-in-the-same-module

ngRos.controller('ShooterSpeedCtrl', function($scope, $controller) {
  $controller('TopicPublisherCtl', {$scope: $scope});
  $scope.message = {left_shooter_speed: 100, right_shooter_speed: 120};
});

$(function(){
  $('#menu-ww-control').addClass('active');
});
