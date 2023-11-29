#include<raylib.h>
#include<stdio.h>
#include<math.h>

#define WIDTH 800
#define HEIGHT 800

// 定义复数类型
typedef struct{	
	double  real;
	double  imag;
}Complex;

// 复平面的范围
double x_min=-1.5, y_min=-1.5;
double x_max=1.5, y_max=1.5;

int max_iteration=100;
int max_module=2;    // 最大模

// 定义迭代常数 C = x+yi
double constant_x=0.5, constant_y=0.5;

int B[256];
int G[256];
int R[256];
Color colors[256];


void matchColor(){ 
	for(int i = 0;i < 256;i++)
	{
		B[i] = i*5%256;
		G[i] = (i+1)*5%256;
		R[i] = (i+2)*5%256;
		colors[i]=(Color){R[i],G[i],B[i],255};//使用了库函数EGERGB 
	}
}

//迭代 
void iteration(Complex num,int round,int nx,int ny,double constant_x,double constant_y){
	double module=num.real*num.real+num.imag*num.imag;    // 模长
	if(module<=max_module&&round<max_iteration){
		Complex b;
		b.real=num.real*num.real-num.imag*num.imag+constant_x;
		b.imag=2*num.real*num.imag+constant_y;
		round++;
		return iteration(b,round,nx,ny,constant_x,constant_y);
	}
	
	if(module>max_module){
		DrawPixel(nx,ny,colors[round]);
		return;
	}
	if(round==max_iteration){
	    DrawPixel(nx,ny,colors[0]);
		return;
	}
	
}	

void Julia(int width,int height,double constant_x,double constant_y){	
	double dx,dy=0;
	dx=(x_max-x_min)/(width-1);
	dy=(y_max-y_min)/(height-1);
	
	// 每像素迭代
	for(int nx=0;nx<width;nx++){
		for(int ny=0;ny<height;ny++){
			int round=0;    // 迭代次数
			Complex x0;
			x0.real=x_min+nx*dx;
			x0.imag=y_min+ny*dy;
			
			// 为单个像素赋予一个值
			iteration(x0,round,nx,ny,constant_x,constant_y);			
		}
	}
}

int main(){
	matchColor();
	char* title = "Julia集的绘制";
	InitWindow(WIDTH,HEIGHT,title);
	SetTraceLogLevel(LOG_WARNING); //在控制台窗口中只显示警告和错误信息
	SetTargetFPS(60);
	
	Julia(WIDTH,HEIGHT,constant_x,constant_y);
	
	// 利用参数生成 C
	double theta = 0;
	
	// 动画部分
	while(!WindowShouldClose()){
		//清屏
		BeginDrawing(); //准备进行帧的绘制
		ClearBackground(WHITE); //清除之前帧绘制的内容
		theta += 0.1;
		constant_x = 0.75*cos(theta);
		constant_y = 0.75*sin(theta);
		
		Julia(WIDTH,HEIGHT,constant_x,constant_y);
		
		if(theta> 2*PI) theta = 0;
		
	    EndDrawing();
	}
		


	return 0;
}


