from flask import Flask, render_template, request, jsonify
import docker
client = docker.from_env()
app = Flask(__name__)

# 配方比例配置
RECIPES = {
    "dumpling": {"water_range": (130, 150), "yeast_ratio": 0, "base_flour": 280},     # 饺子皮
    "noodle": {"water_range": (110, 130), "yeast_ratio": 0, "base_flour": 280},       # 面条
    "steam_bun": {"water_range": (140, 160), "yeast_ratio": 2.8 / 280, "base_flour": 280},  # 馒头
    "pie": {"water_range": (140, 160), "yeast_ratio": 0, "base_flour": 280},          # 馅饼皮
    "bread": {"water_range": (190, 190), "yeast_ratio": 2.9 / 250, "base_flour": 250}  # 面包
}

# 总结表格数据
SUMMARY_TABLE = [
    {"type": "饺子皮", "flour": 280, "water": "130-150", "yeast": 0},
    {"type": "面条", "flour": 280, "water": "110-130", "yeast": 0},
    {"type": "馒头", "flour": 280, "water": "140-160", "yeast": 2.8},
    {"type": "馅饼皮", "flour": 280, "water": "140-160", "yeast": 0},
    {"type": "面包", "flour": 250, "water": "190", "yeast": 2.9}
]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/print')
def print():
    return render_template('airprint.html')

@app.route('/restart', methods=['GET', 'POST'])
def restart_container():
    container_name = 'airprint'  # 你要重启的容器名字
    try:
        container = client.containers.get(container_name)
        container.restart()
        return jsonify({'status': 'success', 'message': f'Container {container_name} restarted successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/mian', methods=['GET', 'POST'])
def mian():
    result = None
    error = None

    if request.method == 'POST':
        try:
            flour = float(request.form['flour'])
            recipe_type = request.form['recipe_type']

            if flour <= 0:
                raise ValueError("面粉量必须大于0")

            ratios = RECIPES.get(recipe_type)
            if not ratios:
                raise ValueError("无效的配方类型")

            base_flour = ratios["base_flour"]

            # 水量区间
            water_min = round(flour * (ratios["water_range"][0] / base_flour), 1)
            water_max = round(flour * (ratios["water_range"][1] / base_flour), 1)

            water_range = (
                str(water_min) if water_min == water_max else f"{water_min}-{water_max}"
            )

            # 酵母
            yeast = round(flour * ratios["yeast_ratio"], 1) if ratios["yeast_ratio"] > 0 else 0

            # 中文类型映射
            result = {
                "flour": flour,
                "water": water_range,
                "yeast": yeast,
                "type": {
                    "dumpling": "饺子皮",
                    "noodle": "面条",
                    "steam_bun": "馒头",
                    "pie": "馅饼皮",
                    "bread": "面包"
                }.get(recipe_type, "未知")
            }

        except ValueError as e:
            error = str(e)
        except:
            error = "请输入有效的数值"

    return render_template('mian.html', result=result, error=error, summary_table=SUMMARY_TABLE)




@app.route('/ddz')
def score():
    return render_template('score.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
